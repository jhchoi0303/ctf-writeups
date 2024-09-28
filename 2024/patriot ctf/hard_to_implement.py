import socket
import time
from pwn import *

# Server details
server_ip = 'chal.competitivecyber.club'
server_port = 6001

# Constants
BLOCK_SIZE = 16

# Enable debug logging
context.log_level = 'debug'

def connect_to_server():
    """ Establish connection to the server. """
    return socket.create_connection((server_ip, server_port))

def send_and_receive(s, message):
    """ Send message to the server and receive response. """
    s.sendall(message + b'\n')
    try:
        response = s.recv(4096)
    except socket.error as e:
        log.error(f"Socket error: {e}")
        return b''
    return response

def receive_until_prompt(s):
    """ Receive data from the server until the challenge prompt is received. """
    data = b""
    while b"Send challenge >" not in data:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk
    return data

def clean_hex(hex_string):
    """ Clean up any non-hexadecimal characters from the string. """
    return ''.join(c for c in hex_string if c in '0123456789abcdefABCDEF')

def ecb_decrypt_with_prefix():
    """ Perform ECB decryption attack using the known prefix 'pctf{'. """
    known_flag = b"pctf{"  # Start with the known prefix

    with connect_to_server() as s:
        # Receive initial server message
        initial_msg = s.recv(4096).decode()
        log.info(f"Initial server message: {initial_msg}")

        for byte_index in range(len(known_flag), BLOCK_SIZE * 3):  # assuming flag length is at most 3 blocks
            block_index = byte_index // BLOCK_SIZE
            pad_length = BLOCK_SIZE - (byte_index % BLOCK_SIZE) - 1

            # Create the payload to align with the flag
            payload = b'A' * pad_length
            receive_until_prompt(s)
            response = send_and_receive(s, payload)

            # Parse and isolate the target block
            try:
                encrypted_hex = response.split(b"Response > ")[1].strip().decode()
                encrypted_hex = clean_hex(encrypted_hex)  # Clean the hex string
                encrypted_blocks = bytes.fromhex(encrypted_hex)
                target_block = encrypted_blocks[block_index * BLOCK_SIZE:(block_index + 1) * BLOCK_SIZE]
                log.debug(f"Target block: {target_block.hex()}")
            except IndexError:
                log.error("Error: Unexpected server response format.")
                log.debug(f"Full response: {response}")
                break
            except ValueError as ve:
                log.error(f"Hex conversion error: {ve}")
                log.debug(f"Hex string: {encrypted_hex}")
                break

            # Try all possible bytes for the unknown byte in the current block
            for i in range(256):
                test_payload = payload + known_flag + bytes([i])
                receive_until_prompt(s)
                test_response = send_and_receive(s, test_payload)

                # Parse and isolate the test block
                try:
                    test_encrypted_hex = test_response.split(b"Response > ")[1].strip().decode()
                    test_encrypted_hex = clean_hex(test_encrypted_hex)  # Clean the hex string
                    test_encrypted_blocks = bytes.fromhex(test_encrypted_hex)
                    test_block = test_encrypted_blocks[block_index * BLOCK_SIZE:(block_index + 1) * BLOCK_SIZE]
                except IndexError:
                    log.error("Error: Unexpected server response format.")
                    log.debug(f"Test response: {test_response}")
                    continue
                except ValueError as ve:
                    log.error(f"Hex conversion error: {ve}")
                    log.debug(f"Test hex string: {test_encrypted_hex}")
                    continue

                # Check if the test block matches the target block
                if test_block == target_block:
                    known_flag += bytes([i])
                    log.info(f"Discovered so far: {known_flag}")
                    break
            else:
                log.warning(f"Byte {byte_index} could not be determined.")
                break

            # Add a small delay to avoid potential rate limiting issues
            time.sleep(0.1)

        return known_flag

if __name__ == "__main__":
    flag = ecb_decrypt_with_prefix()
    log.success(f"\nFlag: {flag.decode('utf-8', errors='ignore')}")