import { render } from "@testing-library/svelte";
import IndexPage from "../../src/routes/+page.svelte";

describe("+page.svelte", async () => {
  test("", async () => {
    const { queryByTestId } = render(IndexPage);

    expect(queryByTestId("pedal-step")).toBe(null);
  });
});
