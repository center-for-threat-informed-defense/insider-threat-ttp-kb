/**
 * Various tweaks to the Read the Docs theme to better conform with 
 * project vision.
 */

// Handle sortable table
$(document).ready( function () {
    $('table.datatable').DataTable();
} );

requirejs.config({
    paths: {
        base: '/static/base',
        plotly: 'https://cdn.plot.ly/plotly-2.12.1.min.js?noext',
    },
});
