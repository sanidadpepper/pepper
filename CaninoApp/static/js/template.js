$('.only-number').keypress(function (e) {
	if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
		return false;
	}
});
tinymce.init({
	selector: 'textarea',
	language: 'es_MX'
});
$('.date').datetimepicker({
	format: 'YYYY-MM-DD'
});