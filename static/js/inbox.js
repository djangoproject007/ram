$(document).ready(function() {
  // scroll instantly to bottom of messages on load
  $(window).scrollTop($(document).height());
  if ($(window).width() < 768) {
    $('#main-nav').remove();
  }

  var sessionKey = $('#sessionKey').text();
  socket = new WebSocket("ws://" + window.location.host + "/chat" + window.location.pathname);

  socket.onmessage = function(message) {
      console.log(message);
      var data = JSON.parse(message.data);

      var currentUser = $('#chatData #user').text();
      var avatar = $('#chatData #avatar').text();
      var html;
      if (data.user != currentUser) {
        html = "<li class='left clearfix'>" +
            "<span class='chat-img pull-left'>" +
                "<a href='/" +data.user +"/'>" +
                "<img src=" + "\'"  + data.avatar + "\'" + " width='45px' height='45px'></a>" +
            "</span>" +
            "<div class='text'>" +
                "<div class='chat-body clearfix'>" +
                    "<div class='header'>" +
                        "<a href='/" +data.user +"/'>" +
                        "<strong class='primary-font'>" + data.user + "</strong></a>" +
                        "<small class='pull-right text-muted'><i class='fa fa-clock-o'></i>" +
                        "now</small>" +
                    "</div>" +
                    "<p>" +
            data.text + "</p></div></li>";
      } else {
        html = "<li class='right clearfix'>" +
            "<span class='chat-img pull-right'>" +
                "<a href='/" +data.user +"/'>" +
                "<img src="  + "\'"  + avatar + "\'" +  " width='45px' height='45px'></a>" +
            "</span>" +
            "<div class='text'>" +
                "<div class='chat-body clearfix'>" +
                    "<div class='header'>" +
                        "<a href='/" +data.user +"/'>" +
                        "<strong class='primary-font'>" + data.user + "</strong></a>" +
                        "<small class='pull-right text-muted'><i class='fa fa-clock-o'></i>" +
                        "now</small>" +
                    "</div>" +
                    "<p>" +
            data.text + "</p></div></li>";
      }
      $("#messages").append(html);

      // scroll instantly to bottom of page upon new message receival
      $(window).scrollTop($(document).height());
  }

  socket.onopen = function() {
      console.log("socked opened");
  }

  // Call onopen directly if socket is already open
  if (socket.readyState == WebSocket.OPEN) socket.onopen();

  $("#messageInput").on('keypress', function(e) {
    if (e.which == 13) {
      var message = {
          user: $('#user').text(),
          message: $('#messageInput').val()
      }

      socket.send(JSON.stringify(message));
      $(this).val('');

      return false;
    }
  });
});
