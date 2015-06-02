$.ajax({
  url: 'serviceStatus.xml',
  type: "GET",
  dataType: "xml",
  success: function (result) {
    console.log(result);
  }
});
