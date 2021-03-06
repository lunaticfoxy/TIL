class MyQueue {
            private int capacity;
            private String[] space;
            private int size = 0;
            private int front = 0;
            private int rear = -1;

            MyQueue(int capacity) {
                this.capacity = capacity;
                this.space = new String[this.capacity];
            }

            boolean isEmpty() {
                if(size == 0) return true;
                else          return false;
            }

            boolean isFull() {
                if(size == capacity) return true;
                else                 return false;
            }

            boolean enQueue(String item) {
                if(isFull())
                    return false;

                rear = (rear + 1) % capacity;
                space[rear] = item;
                size += 1;
                return true;
            }

            String deQueue() {
                String temp = space[front];
                front = (front + 1) % capacity;
                size -= 1;
                return temp;
            }

            int getSize() {
                return size;
            }
        }
