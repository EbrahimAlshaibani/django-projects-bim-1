function genratePDF(){
    const element = document.getElementById("report");
    let options = {
        filename:'تقرير',
        image:{ type: 'jpeg', quality: 1 },
        html2canvas: { scale: 4 },
        jsPDF:{ unit: 'in',
                format: 'letter',
                orientation: 'portrait',
        },
    };
    html2pdf().set(options).from(element).save();
}