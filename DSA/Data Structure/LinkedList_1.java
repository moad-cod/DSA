// Stage 1

public class LinkedList_1<T> {

    T data;
    LinkedList_1<T> next;

    public LinkedList_1(T data) {
        this.data = data;
        this.next = null;
    }
    public static void main(String[] args) {
        LinkedList_1<Integer> node_1 = new LinkedList_1<>(10);
        LinkedList_1<Integer> node_2 = new LinkedList_1<>(20);
        LinkedList_1<Integer> node_3 = new LinkedList_1<>(30);
        LinkedList_1<Integer> node_4 = new LinkedList_1<>(40);

        // Connect the nodes
        node_1.next = node_2;
        node_2.next = node_3;
        node_3.next = node_4;

        // Head
        LinkedList_1<Integer> head = node_1;


        // Traverse
        LinkedList_1<Integer> current = head;

        while (current != null) {
            System.out.print(current.data + " --> ");
            current = current.next;
        }

        System.out.println("null");
    }
}