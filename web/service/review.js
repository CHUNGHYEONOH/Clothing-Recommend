$(function () {

    $(".js-create-review").click(function () {
      $.ajax({
        url: '/service/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-review").modal("show");
        },
        success: function (data) {
          $("#modal-review .modal-content").html(data.html_form);
        }
      });
    });
  
  });