import java.util.PriorityQueue;

public class PriorityQueueE<T> {
    public static void main(String[] args) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        // PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder()); For reverse order priority

        queue.add(30);
        queue.add(10);
        queue.add(20);

        while(!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
    }
}
