$(document).ready(function() {
    // Add item to the list
    $('DIV#add_item').click(function() {
        $('UL.my_list').append('<li>Item</li>');
    });

    // Remove last item from the list
    $('DIV#remove_item').click(function() {
        $('UL.my_list li:last-child').remove();
    });

    // Clear the list
    $('DIV#clear_list').click(function() {
        $('UL.my_list').empty();
    });
});
