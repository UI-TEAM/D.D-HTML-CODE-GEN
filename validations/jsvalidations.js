/*** This file contains code to validations in javascript ***/

/**
* main class
**/
function Validations(){}

/**
* function isObject decides filed need to be filled
* @param object Object
* @returns true or false
**/
Validations.prototype.isObject = function(object){
	return
}

/**
* function objectOf decides recieved object belongs to recieved class prototype
* @param object Object
* @param object prototype
* @returns true or false
**/
Validations.prototype.objectOf = function(object, Class){
	return
}
/**
* Checks if the value is a number.
* @param
* @returns true or false
**/
Validations.prototype.isNumber = function(value) {
  return typeof value === 'number' && !isNaN(value);
}

/**
* Checks if the value is a function.
* @param
* @returns true or false
**/

Validations.prototype.isFunction = function(value) {
  return typeof value === 'function';
}

/**
* Checks if the value is a integer.
* @param
* @returns true or false
**/
Validations.prototype.isInteger = function(value) {
  return this.isNumber(value) && value % 1 === 0;
}

/**
* Checks if the object is an instance of a date
* @param object
* @returns true or false
**/
Validations.prototype.isDate = function(obj) {
  return obj instanceof Date;
}

/**
* Checks if the object is `null` of `undefined`
* @param object
* @returns true or false
**/
Validations.prototype.isDefined = function(obj) {
  return obj !== null && obj !== undefined;
}

/**
* Checks if the object is DOM element
* @param object
* @returns true or false
**/
Validations.prototype.isDomElement = function(o) {
  if (!o) {
    return false;
  }

  if (!this.isFunction(o.querySelectorAll) || !this.isFunction(o.querySelector)) {
    return false;
  }

  if (this.isObject(document) && o === document) {
    return true;
  }

  if (typeof HTMLElement === "object") {
    return o instanceof HTMLElement;
  } else {
    return o &&
      typeof o === "object" &&
      o !== null &&
      o.nodeType === 1 &&
      typeof o.nodeName === "string";
  }
}

/**
* Checks if the object is empty
* @param object
* @returns true or false
**/
Validations.prototype.isEmpty = function(value) {
  var attr;

  // Null and undefined are empty
  if (!this.isDefined(value)) {
    return true;
  }

  // functions are non empty
  if (this.isFunction(value)) {
    return false;
  }

  // Whitespace only strings are empty
  if (this.isString(value)) {
    return v.EMPTY_STRING_REGEXP.test(value);
  }

  // For arrays we use the length property
  if (this.isArray(value)) {
    return value.length === 0;
  }

  // Dates have no attributes but aren't empty
  if (this.isDate(value)) {
    return false;
  }

  // If we find at least one property we consider it non empty
  if (this.isObject(value)) {
    for (attr in value) {
      return false;
    }
    return true;
  }

  return false;
}

/**
* Checks if the value is string
* @param object
* @returns true or false
**/
Validations.prototype.isString = function(value) {
  return typeof value === 'string';
}

/**
* Checks if the value is array
* @param object
* @returns true or false
**/
Validations.prototype.isArray = function(value) {
  return {}.toString.call(value) === '[object Array]';
}

/**
* Checks if the value contains in object
* @param object
* @returns true or false
**/
contains: function(obj, value) {
  if (!this.isDefined(obj)) {
    return false;
  }
  if (this.isArray(obj)) {
    return obj.indexOf(value) !== -1;
  }
  return value in obj;
}