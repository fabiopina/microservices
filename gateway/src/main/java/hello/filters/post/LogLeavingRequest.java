package hello.filters.post;

import javax.servlet.http.HttpServletRequest;
import com.netflix.zuul.context.RequestContext;
import com.netflix.zuul.ZuulFilter;

import hello.filters.HttpRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.Timestamp;

public class LogLeavingRequest extends ZuulFilter {

    private static Logger log = LoggerFactory.getLogger(LogLeavingRequest.class);

    // returns a String that stands for the type of the filter---in this case, pre, or it could be route for a routing filter.
    @Override
    public String filterType() {
        return "post";
    }

    // gives the order in which this filter will be executed, relative to other filters.
    @Override
    public int filterOrder() {
        return 2;
    }

    // contains the logic that determines when to execute this filter (this particular filter will always be executed).
    @Override
    public boolean shouldFilter() {
        return true;
    }

    // contains the functionality of the filter.
    @Override
    public Object run() {
        RequestContext ctx = RequestContext.getCurrentContext();
        HttpServletRequest request = ctx.getRequest();

        Timestamp timestamp = new Timestamp(System.currentTimeMillis());

        log.info(String.format("FROM-> %s TO-> %s METHOD-> %s", request.getRemoteAddr(), request.getRequestURL().toString(), request.getMethod()));
        HttpRequest.post(timestamp.toString(), "LEAVING", String.format("FROM-> %s TO-> %s METHOD-> %s", request.getRemoteAddr(), request.getRequestURL().toString(), request.getMethod()));

        return null;
    }
}
