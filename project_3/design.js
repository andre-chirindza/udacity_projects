/**
 * @author @andre-chirindza
 * @description Final project of Nonedegree Intro to Programming 
 * @copyright Udacity
 * @version 1.0.0
 */


/**
 * Adding a listener for a document
 */
document.addEventListener("DOMContentLoaded", init, false);

/**
 * Select the width and height
 * @params void
 * @returns {object} dimentions
 **/
function getDimentions() {
    var width = document.getElementById("pixel-width");
    var height = document.getElementById("pixel-height");
    
    if (typeof width.value === 'undefined' || typeof height.value === 'undefined' ||
        parseInt(width.value) < 1 || parseInt(height.value) < 1) {
        width.classList.add("alert-danger");
        height.classList.add("alert-danger");
    } else {
        return {
            width: width.value,
            height: height.value,
        };
    }
}

/**
 * Create Table
 * @param {int} rows The date
 * @param {int} columns The string
 * @returns {object} table
 */
function createTable(rows, columns) {
    var table = document.getElementById("pixelCanvas");

    //Styling the table
    table.setAttribute("class", "table table-bordered mt-10");
    
    var tbody = document.createElement("tbody");
    tbody.setAttribute("id", "tableBody");

    for (let i = 0; i < rows; i++) {
        var tr = document.createElement("tr");
        tr.setAttribute("id", "table-row-" + (i + 1));

        for (let index = 0; index < columns; index++) {
            var td = document.createElement("td");
            td.setAttribute("id", "table-column-" + (index + 1));
            td.setAttribute('class', 'p-3')
            addEventListeners(td);
            tr.appendChild(td);
        }

        tbody.appendChild(tr);
    }
    table.appendChild(tbody);

    return table;
}

/**
 * Add Table
 * @param void
 * @param void
 * @returns void
 */
function addTable() {
    var dimentions = getDimentions();
    var divContainer = document.getElementById("tableBox");
    var pixelCanvas = document.getElementById("pixelCanvas");
    var tableBody = document.getElementById('tableBody');
    
    if (typeof dimentions !== 'undefined') {
        var table = createTable(dimentions.width, dimentions.height);
        
        if (tableBody === null) {
            divContainer.appendChild(table);
        } else {
            pixelCanvas.removeChild(tableBody);
            divContainer.appendChild(table);
        }
    }
}


/**
 * Add event to table td 
 * @param {object} td
 * @returns void
 */
function addEventListeners(td) {
    td.addEventListener('click', function () {
        var color = document.getElementById('colorPicker').value
        this.hasAttribute('style') ?
            this.removeAttribute('style') :
            this.setAttribute('style', 'background-color: ' + color + '; border-color: ' + color + ';');
    });
}


/**
 * Remove class in the given attribute
 * @param void
 * @returns void
 */
function design() {
    addTable()
}

/**
 * Trigged when the Dom content is loaded
 * @param void
 * @returns void
 */
function init() {
    var submit = document.getElementById("submit");
    submit.addEventListener("click", design, false);
}