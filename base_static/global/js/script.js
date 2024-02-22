document.addEventListener("DOMContentLoaded", function() {
  const containersGrupo = document.querySelectorAll(".container-grupo");

  containersGrupo.forEach(containerGrupo => {
    containerGrupo.addEventListener("click", function() {
      const temaGrupo = this.getAttribute("tema-grupo");

      window.location.href = `/flashcard/criacao/tipo/${temaGrupo}`;
    });
  });
});

function flipCard(element) {
  let card = element.querySelector('.flashcard');
  card.style.transform = card.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';
}



