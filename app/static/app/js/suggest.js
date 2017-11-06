$().ready(function() {
    $('#suggestion').keyup(function(){
        var query
        query = $(this).val()
        $.post('/app/suggest/', {suggestion: query}, function(data){
            $('#authors').html(data)
        })
    })
})
