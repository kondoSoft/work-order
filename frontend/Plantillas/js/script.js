$(document).ready(function (){
  $("#check").iCheck({
    checkboxClass:"icheckbox_minimal"
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
   } );
})
