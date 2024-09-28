from pwn import *
import base64
import time
#context.log_level = 'debug'
# Define the target server and port
server = 'chal.pctf.competitivecyber.club'
port = 9001

# Connect to the remote server using pwntools
conn = remote(server, port)

def decode_challenge(challenge):
    # Step 1: Base64 decode the challenge once to get (encoded|n)
    decoded_once = base64.b64decode(challenge).decode()

    # Extract the encoded data and the number of decodings
    try:
        encoded, n = decoded_once.split('|')
        n = int(n)
    except ValueError:
        print("Error: Incorrectly formatted challenge. Expected format '(encoded|n)'.")
        return None

    # Step 2: Decode the data 'n' number of times
    for _ in range(n):
        encoded = base64.b64decode(encoded).decode()

    return encoded

# Read and respond to challenges
try:
    while True:
        # Read the combined challenge and iteration response from the server
        response = conn.recv().decode().strip()
        #print(f"Received: {response}")  # Print server response for debugging

        # Split the response into parts by newlines
        parts = response.split('\n')
        #print(f"Split Parts: {parts}")  # Debugging output for parts received

        # Ensure there are sufficient parts to process the challenge and iteration info
        if len(parts) < 2:
            print(f"Error: Expected challenge and iteration, but got {len(parts)} parts. Re-syncing...")
            continue

        # Extract the challenge and iteration from the last two parts
        try:
            if(len(parts)>=3):
                challenge_line = parts[-2]
                iteration_line = parts[-1]

            else:
                challenge_line = parts[0]
                iteration_line = parts[1]

            # Extract the challenge part from the challenge_line
            if 'Challenge: ' in challenge_line:
                challenge = challenge_line.split('Challenge: ')[1].strip()
                print(f"Extracted Challenge: {challenge}")  # Debugging output
            else:
                print(f"FLAG: {response}")
                continue

            # Extract the current iteration from the iteration_line
            # The format is (current_iteration/1000) >>
            iteration_part = iteration_line.split('(')[1].split(')')[0]  # Extracts current_iteration/1000
            current_iteration = iteration_part.split('/')[0]
            print(f"Current Iteration: {current_iteration}")  # Debugging output

            # Decode the challenge
            decoded_response = decode_challenge(challenge)
            if decoded_response is None:
                print("Skipping due to decoding error.")
                continue

            print(f"Decoded Response: {decoded_response}")  # Debugging output

            # Construct the answer using the decoded response and the current iteration number
            answer = f"{decoded_response}|{current_iteration}"
            print(f"Sending Response: {answer}")  # Debugging output

            # Send the answer back to the server
            conn.sendline(answer)


            # Add a short sleep to handle network latency or server delays
            time.sleep(0.3)

        except Exception as e:
            print(f"Error during parsing or challenge processing: {e}")
            continue

        # Check for incorrect or correct response feedback
        #feedback = conn.recvline().decode().strip()
        #print(feedback)
        #if 'correct' in feedback.lower():
           # print("Challenge completed successfully!")
            #break
        #elif 'incorrect' in feedback.lower():
            #print("Incorrect response. Exiting.")
            #break

finally:
    conn.close()