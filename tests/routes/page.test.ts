import { render } from "@testing-library/svelte";
import IndexPage from "../../src/routes/+page.svelte";

describe("トップページのテスト", async () => {
  test("ペダル数が0の場合はペダルステッパーが1つも表示されない", async () => {
    vi.mock("store/pedal", async () => {
      const { writable } = await import("svelte/store");
      return writable([]);
    });

    const { queryByTestId } = render(IndexPage);

    expect(queryByTestId("pedal-step")).toBe(null);
  });

  // test("ペダル数が1の場合はペダルステッパーが1つ表示される", async () => {
  //   vi.mock("store/pedal", async () => {
  //     const { writable } = await import("svelte/store");
  //     return writable([
  //       { id: "dadfb805-2ed1-483e-88e5-fe69da8513fb", name: "", kind: "distortion", parameters: { gain: 1 } },
  //     ]);
  //   });

  //   const { getByTestId } = render(IndexPage);

  //   expect(getByTestId("pedal-step"));
  // });
});
