# Instagram Crawler

Este crawler coleta informações do perfis de instagram em um determinado período de tempo e salvar elas em arquivos txt para uma futura análise.
<h3> O que é coletado? </h3>
<p> As informações que são coletadas pelo crawler são:
  <ul>
    <li> Número de Pessoas que estão seguindo o perfil (Seguidores)</li>
    <li> Número de Pessoas que o Perfil Segue (Seguindo) </li>
    <li> Número de Mídias (Fotos, vídeos e IGTV) </li>
    <li> Mostrar as últimas 11 mídias postada pelo perfil 
      <ul>
        <li> ID da mídia </li>
        <li> Número de Curtidas </li>
        <li> Número de Comentários </li>
        <li> Data e Horário da Publicação </li>
        <li> Legenda da mídia </li>
        <li> Descrição Feita Pela Inteligência Artifical do Instagram </li>
        <li> URL da mídia </li>
      </ul>
    </li>
  </ul>
</p>
<h3> Intervalo de Coleta </h3>
<p>O intervalo entre cada coleta é definido na variável "tempo", deve ser colocada o tempo em segundos.
Recomendado um intervalo acima de 2 horas no caso de análise de muito perfis.</p>
<p> Além do intervalo entre cada coleta, tem o intervalo entre os perfis, tem um delay aleatório de 3 a 10 segundos entre a coleta dos perfis. </p>
<h3> Estrutura de Arquivos </h3>
<p> Para cada perfil é criado uma pasta no diretório Coleta, nessa pasta serão salvas todas as coletas. <p>
<p> Os arquivos gerados e salvos na pasta do perfil, são salva com a seguinte nomenclatura: "nomedoperfil"+"timestamp"+".txt".
  O timestamp é um código com a data e o horário da coleta. </p>
