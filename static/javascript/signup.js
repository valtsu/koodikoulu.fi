$(function() {
  var $form = $('form#signup-form')
  var $submits = $form.find('[type=submit]')
  var $spinner = $form.find('.spinner')

  function formState($form) {
    return R.mergeAll(
      $form.serializeArray().map(function(o) {
        var obj = {}
        obj[o.name] = o.value
        return obj
    }))
  }

  var requiredKeys = $form.find('label.required')
    .map(function(i, el) {
      return $(el).attr('for').split('_')[1]
    }).get()

  $form.find('input').keyup(function() {
    var data = formState($form)

    var formValid = requiredKeys.map(function(key) {
      return !R.isEmpty(data[key])
    }).reduce(function(a, b) { return a && b })

    $submits.prop('disabled', !formValid)
  })

  $form.submit(function(e) {
    e.preventDefault()
    $form.find('.submit-message').hide()
    $spinner.show()
    $submits.prop('disabled', true)

    $.ajax({
      url: $form.attr('action'),
      type: $form.attr('method'),
      data: $form.serialize(),

      success: function(res) {
        $spinner.hide()
        $form.trigger('reset')
        $submits.prop('disabled', false)
        $form.find('.submit-message.success').show()
      },

      error: function(res) {
        $spinner.hide()
        $submits.prop('disabled', false)
        $form.find('.submit-message.error').show()
      }
    })
  })

})
