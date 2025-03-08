import threading
import hashlib
import time
import random

NUM_THREADS = 24

def mine_block(thread_id, prefix_zeros=4):
    print(f"🚀 Thread {thread_id} เริ่มขุด Bitcoin")
    
    start_time = time.time()
    while True:
        nonce = random.randint(0, 999999999)
        data = f"Thread-{thread_id}:{nonce}".encode()
        hash_result = hashlib.sha256(data).hexdigest()

        if hash_result.startswith("0" * prefix_zeros):
            print(f"✅ Thread {thread_id} พบ Nonce: {nonce}")
            print(f"🔗 Hash: {hash_result}")
            print(f"⏳ ใช้เวลา: {time.time() - start_time:.2f} วินาที\n")
            break

threads = []
for i in range(NUM_THREADS):
    thread = threading.Thread(target=mine_block, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("🎉 การขุดเสร็จสิ้น!")
print("ยินดีด้วยเศรษฐีหน้าใหม่ คุณได้รับ Bitcoin 1000 BTC แล้ว")