/** @type {import("./$types").PageLoad} */
export function load({ params }) {
  return {
    effect: params.effect,
  };
}
