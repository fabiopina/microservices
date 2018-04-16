package hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.context.annotation.Bean;
import hello.filters.pre.LogIncomingRequest;
import hello.filters.post.LogLeavingRequest;

@EnableZuulProxy
@SpringBootApplication
public class GatewayApplication {

  public static void main(String[] args) {
    SpringApplication.run(GatewayApplication.class, args);
  }

  @Bean
  public LogIncomingRequest logIncomingRequest() {
    return new LogIncomingRequest();
  }

  @Bean
  public LogLeavingRequest logLeavingRequest() {
    return new LogLeavingRequest();
  }

}
