class DynamicArray {
private:
    int* arr;
    int capacity;
    int size;

public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->arr = new int[capacity];
    }

    int get(int i) {
        return this->arr[i];
    }

    void set(int i, int n) {
        this->arr[i] = n;
    }

    void pushback(int n) {
        if(this->size == this->capacity){
            this->resize();
        }
        this->arr[this->size] = n;
        this->size++;
    }

    int popback() {
        this->size--;
        int pop = this->arr[this->size];
        return pop; 
    }

    void resize() {
        this->capacity *= 2;
        int* new_arr = new int[this->capacity];
        for(int i = 0; i < this->size; i++){ 
            new_arr[i] = this->arr[i];
        }
        delete[] this->arr;
        this->arr = new_arr;
    }

    int getSize() {
        return this->size;
    }

    int getCapacity() {
        return this->capacity; 
    }
};
