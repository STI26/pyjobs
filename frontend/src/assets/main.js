function setObjFields (objFields, data) {
  Object.keys(data).forEach(key => {
    if (key in objFields) {
      objFields[key] = data[key]
    }
  })
}
function setErrorFields (objFields, data) {
  Object.keys(data).forEach(key => {
    if (key in objFields) {
      console.log('key', key)
      objFields[key] = data[key][0]
    } else {
      objFields.nonFieldErrors = data[key][0]
    }
  })
}
function clearObjectFields (objFields) {
  Object.keys(objFields).forEach(key => {
    objFields[key] = ''
  })
}

export { setObjFields, setErrorFields, clearObjectFields }
