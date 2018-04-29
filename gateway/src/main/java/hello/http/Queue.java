package hello.http;

import java.util.Vector;

public class Queue {
    private Vector<String> requestQueue;

    public Queue() {
        requestQueue = new Vector<>();
    }

    public void add(String element) {
        requestQueue.add(element);
    }

    public void start() {
        Thread thread = new Thread(new Runnable() {
            public void run()
            {
                while (true) {
                    if(!(requestQueue.isEmpty())) {
                        HttpRequest.post(requestQueue.get(0));
                        requestQueue.remove(0);
                    }
                }

            }});
        thread.start();
    }
}
