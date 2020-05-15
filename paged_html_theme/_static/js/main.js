console.log("Starting to load scripts");
requirejs(["config.js"], function(util) {
    console.log("Loaded config.js");
});
requirejs(["paged.js"], function(util) {
    console.log("Loaded paged.js");
});
requirejs(["load_mathjax.js"], function(util) {
    console.log("Loaded load_mathjax.js");
});