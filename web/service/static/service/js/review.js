console.log("fuck");

$(function (){
  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-review .modal-content").html("");
        $("#modal-review").modal("show");
      },
      success: function (data) {
        $("#modal-review .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("hi!");
          $("#review-table tbody").html(data.html_review);
          $("#modal-review").modal("hide");
        }
        else {
          $("#modal-review .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  $(".js-create-review").click(loadForm);
  $("#modal-review").on("submit", ".js-review-create-form", saveForm);
});