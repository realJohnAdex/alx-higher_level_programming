$(document).ready(function() {
    $('#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    });
});
