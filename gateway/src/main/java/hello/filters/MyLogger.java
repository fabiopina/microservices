package hello.filters;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class MyLogger {

    Logger logger = Logger.getLogger("MyLog");
    FileHandler fh;

    public MyLogger() {

        try {
            // This block configure the logger with handler and formatter
            fh = new FileHandler("EventSequence.txt");
            logger.addHandler(fh);
            logger.setUseParentHandlers(false);
            SimpleFormatter formatter = new SimpleFormatter();
            fh.setFormatter(formatter);

        } catch (SecurityException | IOException e) {
            e.printStackTrace();
        }

    }

    public void write(String message){
        logger.info(message);
    }
}
