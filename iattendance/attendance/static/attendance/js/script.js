$(document).ready(function(){

	$(".date-picker").nepaliDatePicker({
      dateFormat: "%y/%m/%d",
      closeOnDateSelect: true, 
      
  });

	$('#table_id').DataTable();

	
});

