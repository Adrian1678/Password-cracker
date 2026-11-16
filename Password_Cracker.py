import hashlib
import threading
import argparse
#setting up argparse to make it easy to use from the terminal
parser=argparse.ArgumentParser(description="Password Cracker")
parser.add_argument("-a","--algorithm")
parser.add_argument("-t","--target")
parser.add_argument("-w","--wordlist")
args=parser.parse_args()
#setting up the threads
t=threading.Event()

#function that compare our hash to the wordlist
def check_password(password, target_hash,algorithm):
    if t.is_set():
        return
    hashed = hashlib.new(algorithm, password.encode()).hexdigest()
    if hashed == target_hash:
        t.set()
        print(f"cracked!password is {password}")
    else:
        return False
    #creating the algorithm to take different hash types
algorithm= args.algorithm
target_hash=args.target#hahed password
wordlist=args.wordlist
#opening a file and sending every word trough the function/ also making threads to make it faster.
with open(wordlist, "r") as file:
    
    thread_list=[]
    for word in file:
        #making sure it only reads one word per line
        word= word.strip()
        if t.is_set():
            break

        threads=threading.Thread(target=check_password, args=(word, target_hash, algorithm))
        thread_list.append(threads)
        threads.start()
    for thread in thread_list:
        thread.join()