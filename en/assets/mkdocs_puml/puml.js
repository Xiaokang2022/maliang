// Wide diagrams receive enormously big height. This code
// assigns a special class .wide-svg to each svg where width > height
// and CSS fixes the problem.
document.addEventListener("DOMContentLoaded", function() {
    const svgs = document.querySelectorAll('.puml .diagram');
    svgs.forEach(svg => {
        // Get the computed width and height of each SVG
        // const rect = svg.querySelector('rect');
        let width = svg.getAttribute('width');
        let height = svg.getAttribute('height');

        width = parseInt(width);
        height = parseInt(height);

        if(isNaN(width) || isNaN(height)) {
            return
        }

        if (width > height) {
            svg.classList.add('wide-svg');
        }
    });
});
