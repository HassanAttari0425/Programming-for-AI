$(document).ready(function () {
    $('#userInput').on('input', function () {
      const input = $(this).val();
      if (input.length > 2) {
        $.ajax({
          url: "/suggest",
          method: "POST",
          contentType: "application/json",
          data: JSON.stringify({ input }),
          success: function (data) {
            let html = '';
            data.suggestions.forEach(item => {
              html += `<div class="suggestion-item">${item}</div>`;
            });
            $('#suggestions').html(html).show();
          }
        });
      } else {
        $('#suggestions').hide();
      }
    });
  
    $(document).on('click', '.suggestion-item', function () {
      const text = $(this).text();
      $('#userInput').val(text);
      $('#suggestions').hide();
    });
  });
  
  function sendMessage() {
    const message = $('#userInput').val();
    $('#chat').append(`<p><b>You:</b> ${message}</p>`);
    $.ajax({
      url: "/get_response",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({ message }),
      success: function (data) {
        $('#chat').append(`<p><b>Chatbot:</b> ${data.response}</p>`);
        $('#userInput').val('');
        $('#suggestions').hide();
      }
    });
  }
  