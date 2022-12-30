function abnormality() {
  const targets = [undefined, null, ""];
  targets.forEach(target => {
    console.log(`mention:${target}, result:${CreateMensions(target)}`);
  });
}

function here() {
  const targets = "here";
  console.log(`mention:${targets}, result:${CreateMensions(targets)}`);
}

function everyone() {
  const targets = "everyone";
  console.log(`mention:${targets}, result:${CreateMensions(targets)}`);
}

function single() {
  const targets = "1031000015751106591";
  console.log(`mention:${targets}, result:${CreateMensions(targets)}`);
}

function multiple() {
  const targets = ["1031000015751106591", "822975666734760008"];
  console.log(`mention:${targets}, result:${CreateMensions(targets)}`);
}

function mixture() {
  const targets = ["1031000015751106591", "here", "everyone", "822975666734760008"];
  console.log(`mention:${targets}, result:${CreateMensions(targets)}`);
}
