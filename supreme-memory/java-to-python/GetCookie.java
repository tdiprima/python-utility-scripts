/**
 * It's just a tiny block of json posted to /user/login
 * At this point, your http client would have a session cookie.
 * Nothing else should have to be changed.
 */
import org.eclipse.jetty.client;
// etc...

class GetToken {
    public static void main(String[] args) {
        String server = "quip_server";
        String url = server + "/user/login?_format=json";

        String username = "";
        String password = "";
        String auth = "{\"name\":\"" + username + "\", \"pass\": \"" + password + "\"}";

        try {
            response = wc2.newRequest(url).method("POST")
                    .content(new StringContentProvider(auth), "application/json").timeout(600, TimeUnit.SECONDS)
                    .header(HttpHeader.CONTENT_TYPE, "application/json")
                    .send();
        } catch (InterruptedException | TimeoutException | ExecutionException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
