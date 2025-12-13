function copyToClipboard() {
    const resultText = document.getElementById('resultText').value;
    if (!resultText) return;

    navigator.clipboard.writeText(resultText).then(() => {
        const btn = document.getElementById('copyBtn');
        btn.style.color = "#27ae60";
        btn.innerHTML = '<i class="fas fa-check"></i>';

        setTimeout(() => {
            btn.style.color = "";
            btn.innerHTML = '<i class="fas fa-copy"></i>';
        }, 2000);
    });
}

function clearFields() {
    document.querySelector('textarea[name="text"]').value = '';
    const resultText = document.getElementById('resultText');
    if (resultText) resultText.value = '';

    const copyBtn = document.getElementById('copyBtn');
    if (copyBtn) copyBtn.style.display = 'none';

    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }
}

async function pasteToInput() {
    try {
        const text = await navigator.clipboard.readText();
        const textarea = document.querySelector('textarea[name="text"]');
        textarea.value = text;
        const pasteBtn = document.querySelector('.paste-icon');
        const originalColor = pasteBtn.style.color;
        pasteBtn.style.color = "#27ae60";
        setTimeout(() => {
            pasteBtn.style.color = "";
        }, 500);
    } catch (err) {
        console.error('Failed to read clipboard contents: ', err);
        alert('Failed to paste from clipboard. Please allow clipboard permissions.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', () => {
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        });
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
    });
});
