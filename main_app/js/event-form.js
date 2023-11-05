document.addEventListener('DOMContentLoaded', function () {
    const descriptionInput = document.querySelector('#id_description');
    const characterCountElement = document.createElement('div');

    descriptionInput.parentNode.appendChild(characterCountElement);

    function updateCharacterCount() {
      const characterCount = descriptionInput.value.length;
      const maxCharacterCount = 250; 
      characterCountElement.textContent = `Character Count: ${characterCount}/${maxCharacterCount}`;
    }

    descriptionInput.addEventListener('input', updateCharacterCount);

    const initialCharacterCount = descriptionInput.getAttribute('data-character-count');
    if (initialCharacterCount) {
      characterCountElement.textContent = `Character Count: ${initialCharacterCount}`;
    } else {
      updateCharacterCount(); 
    }
  })