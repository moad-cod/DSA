import java.util.ArrayList;

public class Queue<T> {
    private ArrayList<T> items;

    public Queue() {
        items = new ArrayList<>();
    }

    public void enqueue(T item) {
        items.add(item);
    }

    public T dequeue() {
        if (items.isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return items.remove(0);
    }

    public T peek() {
        if (items.isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return items.get(0);
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public int size() {
        return items.size();
    }

    public boolean search(T item) {
        return items.contains(item);
    }

    
    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();

        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        System.out.println(queue.size());
        System.out.println(queue.search(10));
        System.out.println(queue.search(50));
        System.out.println(queue.peek());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        System.out.println(queue.size());
    }
}
