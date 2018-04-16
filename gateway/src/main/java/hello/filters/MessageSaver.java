package hello.filters;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

public class MessageSaver {
    String state;
    File file;

    public MessageSaver(String state) {
        this.state = state;
        file = new File("EventSequence.txt");
        file.getParentFile().mkdirs();

        /*try (this.writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("filename.txt"), "utf-8"))) {

        } catch (IOException e) {
            e.printStackTrace();
        }*/


    }

    public void write(String message){
        try {
            PrintWriter pw = new PrintWriter(file);
            pw.println(message);
            pw.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
