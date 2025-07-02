#!/usr/bin/haserl
<%in p/common.cgi %>

<%
page_title="Wireguard Editor"
config_file="/root/wireguard"

if [ "$REQUEST_METHOD" = "POST" ]; then
    case "$POST_action" in
        editconfig)
            NEW_CONTENT="$POST_content"
            if printf "%s" "$NEW_CONTENT" > "$config_file"; then
                redirect_back "success" "Config file updated successfully"
            else
                redirect_back "error" "Failed to write config file"
            fi
            exit
            ;;
    esac
    exit
fi
%>

<%in p/header.cgi %>

<div class="row g-4">
    <div class="col-12 col-md-6">
        <!-- Config Editor -->
        <form action="<%= $SCRIPT_NAME %>" method="post">
            <% field_hidden "action" "editconfig" %>
            <div class="mb-3">
                <label class="form-label">Edit /root/wireguard:</label>
                <textarea class="form-control font-monospace w-100" 
                         name="content" 
                         rows="20"
                         style="width: 100%"><%
                    if [ -f "$config_file" ]; then
                        cat "$config_file" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g'
                    else
                        echo "Config file not found!"
                    fi
                %></textarea>
            </div>
            <% button_submit "Save Changes" "primary" %>
        </form>
    </div>

    <div class="col-12 col-md-6">
        <!-- File displays -->
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 p-0">
                <h6 class="text-muted">/etc/wireguard.conf</h6>
            </div>
            <div class="card-body p-0">
                <pre class="m-0"><% ex "cat /etc/wireguard.conf" %></pre>
            </div>
        </div>

        <div class="card border-0">
            <div class="card-header bg-transparent border-0 p-0">
                <h6 class="text-muted">/etc/network/interfaces.d/wg0</h6>
            </div>
            <div class="card-body p-0">
                <pre class="m-0"><% ex "cat /etc/network/interfaces.d/wg0" %></pre>
            </div>
        </div>
    </div>
</div>

<%in p/footer.cgi %>