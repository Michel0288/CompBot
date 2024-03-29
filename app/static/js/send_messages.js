let message = $("#message-to-send");
let sender = $("#message-sender");
sender.on("click", ()=>{
    if($.trim(message.val()).length != 0){
        $("#chatbox").append(`
            <!-- THIS IS YOUR MESSAGE -->
            <div class="message message-out">
                <a href="#" data-bs-toggle="modal" data-bs-target="#modal-profile" class="avatar avatar-responsive">
                    <img class="avatar-img" src="../static/assets/img/avatars/1.jpg" alt="">
                </a>

                <div class="message-inner">
                    <div class="message-body">
                        <div class="message-content">
                            <div class="message-text">
                                <p>`+ $.trim(message.val()) +`</p>
                            </div>
                        </div>
                    </div>

                    <div class="message-footer">
                        <span class="extra-small text-muted">`+ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) +`</span>
                    </div>
                </div>
            </div>

            <!-- THIS IS THE BOT TYPING -->
            <div id="remove-typing" class="message">
                <a href="#" class="avatar avatar-responsive">
                    <img class="avatar-img" src="../static/assets/img/avatars/2.jpg" alt="">
                </a>

                <div class="message-inner">
                    <div class="message-body">
                        <div class="message-content">
                            <div class="message-text">
                                <p>CompBot is typing<span class="typing-dots"><span>.</span><span>.</span><span>.</span></span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `)
        message.val("");

        setTimeout( function(){ 
            $("#remove-typing" ).remove();
            $("#chatbox").append(` 
                <!-- THIS IS THE BOT REPLY -->
                <div class="message">
                    <a href="#" class="avatar avatar-responsive">
                        <img class="avatar-img" src="../static/assets/img/avatars/2.jpg" alt="">
                    </a>

                    <div class="message-inner">
                        <div class="message-body">
                            <div class="message-content">
                                <div class="message-text">
                                    <p>Hey, Michel! YOUR ANSWER IS GIMME 50 GRAND !!</p>
                                </div>
                            </div>
                        </div>

                        <div class="message-footer">
                            <span class="extra-small text-muted">`+ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) +`</span>
                        </div>
                    </div>
                </div>
                `);
        }  , 3000 );
    }
});