$().ready(function() {
    $('#checkall').click(function() {
        val = this.checked
        $("input[id^='check-']").each(function() {
            this.checked = val
        })
    })

    $('#checkall-selected').click(function() {
        val = this.checked
        $("input[id^='selected-check-']").each(function() {
            this.checked = val
        })
    })

    $('#add_selected').click(function() {
        var selected_ids = []
        $('.book:checked').each(function() {
            id = $(this).attr('id').replace('check-', '')
            selected_ids.push(id)
        })

        $.post('/app/select_books/', {'selected_ids': selected_ids}, function(data){
            $('#selected_books').html(data)
            $('#run_tests').prop('disabled', false)
        })
    })

    $('#remove_selected').click(function() {
        var removed_ids = []
        $('.selected-book:checked').each(function() {
            id = $(this).attr('id').replace('selected-check-', '')
            removed_ids.push(id)
        })

        $.post('/app/select_books/', {removed_ids: removed_ids}, function(data){
            $('#selected_books').html(data)
            $('#checkall-selected').prop('checked', false)
        })
    })

    $('#run_tests').click(function() {
        var ids = []
        $('.selected-book').each(function() {
            id = $(this).attr('id').replace('selected-check-', '')
            ids.push(id)
        })

        if (ids.length > 0) {
            $.post('/app/run_tests/', {'ids': ids}, function(data){
                $('#run_tests').prop('disabled', true)
            })
        }
    })
})
