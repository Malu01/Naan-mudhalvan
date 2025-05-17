<script>
document.getElementById('recommendForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const movie = document.getElementById('movieName').value;
  fetch('/recommend', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `movieName=${movie}`
  })
  .then(res => res.json())
  .then(data => {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<h3>Recommended Movies:</h3><ul>' +
      data.map(m => `<li>${m}</li>`).join('') + '</ul>';
  })
  .catch(() => {
    document.getElementById('result').innerHTML = '<p>Error retrieving recommendations.</p>';
  });
});
</script>
