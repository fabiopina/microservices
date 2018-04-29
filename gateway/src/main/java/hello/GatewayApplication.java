package hello;

import hello.http.Queue;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.context.annotation.Bean;
import hello.filters.pre.LogIncomingRequest;
import hello.filters.post.LogLeavingRequest;
import hello.http.Queue;

@EnableZuulProxy
@SpringBootApplication
public class GatewayApplication {
  static Queue q = new Queue();

  public static void main(String[] args) {
    q.start();
    SpringApplication.run(GatewayApplication.class, args);
  }

  @Bean
  public LogIncomingRequest logIncomingRequest() {
    return new LogIncomingRequest(q);
  }

  @Bean
  public LogLeavingRequest logLeavingRequest() {
    return new LogLeavingRequest(q);
  }

}
