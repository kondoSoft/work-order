$(document).ready(function (){
  $("#check").iCheck({
    checkboxClass:"icheckbox_square-green"
  })
  $('#work-orders').DataTable( {
       columnDefs: [ {
           targets: [ 0 ],
           orderData: [ 0, 1 ]
       }, {
           targets: [ 1 ],
           orderData: [ 1, 0 ]
       }, {
           targets: [ 4 ],
           orderData: [ 4, 0 ]
       } ]
   } )
   $('input[name="daterange"]').daterangepicker();
   $(".filters").select2({
     id: 'prueba'
   });
   $(".tooltip").tooltip();
   $(".filter-toggle").on("click", function(){
     $(".filters-containers").fadeToggle(400)
   })
     $("#slimScrollDiv").slimScroll();
})
