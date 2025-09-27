let copySvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy">
<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
</svg>
`;

let checkSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check green">
<path d="M20 6 9 17l-5-5"/>
</svg>
`;

let downloadSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-download">
<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>
</svg>
`;

let controls = `
<div class="control">
    <button class="icon-button puml-copy">
        ${copySvg}
    </button>
    <button class="icon-button puml-download">
        ${downloadSvg}
    </button>
    <hr />
    <button class="icon-button puml-zoom-in">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-plus">
        <path d="M5 12h14"/><path d="M12 5v14"/>
        </svg>
    </button>
    <button class="icon-button puml-zoom-reset">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-house">
        <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
        </svg>
    </button>
    <button class="icon-button puml-zoom-out">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-minus">
        <path d="M5 12h14"/>
        </svg>
    </button>
</div>
`;

function processDiagrams() {
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

        const g = svg.querySelector('g');
        const panzoom = Panzoom(g, {canvas: true});

        g.parentElement.addEventListener('wheel', function (event) {
            if (!event.shiftKey) return
            // Panzoom will automatically use `deltaX` here instead
            // of `deltaY`. On a mac, the shift modifier usually
            // translates to horizontal scrolling, but Panzoom assumes
            // the desired behavior is zooming.
            panzoom.zoomWithWheel(event)
        });

        svg.insertAdjacentHTML("beforebegin", controls);

        const control = svg.parentElement.querySelector(".control");
        const copyBtn = control.querySelector(".puml-copy");
        const downloadBtn = control.querySelector(".puml-download");
        const zoomResetBtn = control.querySelector(".puml-zoom-reset");
        const zoomInBtn = control.querySelector(".puml-zoom-in");
        const zoomOutBtn = control.querySelector(".puml-zoom-out");

        zoomResetBtn.addEventListener("click", event => {
            panzoom.reset({animate: false});
        });
        zoomInBtn.addEventListener("click", event => {
            panzoom.zoomIn();
        });
        zoomOutBtn.addEventListener("click", event => {
            panzoom.zoomOut();
        });

        let timeout = null;
        copyBtn.addEventListener("click", event => {
            clearTimeout(timeout);

            let btn = event.target.closest('button');
            btn.innerHTML = checkSvg;

            timeout = setTimeout(() => {
                btn.innerHTML = copySvg;
            }, 1500);
        });
        copyBtn.addEventListener("click", e => {
            const svgString = new XMLSerializer().serializeToString(svg);
            // Copy svg as text
            navigator.clipboard.writeText(svgString);
        });
        downloadBtn.addEventListener("click", e => {
            const svgString = new XMLSerializer().serializeToString(svg);
            let blob = new Blob([svgString], { type: 'image/svg+xml' });
            let link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'diagram.svg';
            link.click();
            URL.revokeObjectURL(link.href);
        });
    });
}

// This checks if mkdocs-material is installed, use document$.subscribe.
// Otherwise, add listener to DOMContentLoaded
if (typeof document$ !== 'undefined' && document$.subscribe){
    document$.subscribe(processDiagrams);
} else {
    document.addEventListener('DOMContentLoaded', processDiagrams);
}
