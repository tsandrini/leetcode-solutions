# --- nix/parts/treefmt/treefmt.nix
{
  pkgs,
  projectPath,
  ...
}: {
  package = pkgs.treefmt;
  flakeCheck = true;
  flakeFormatter = true;
  projectRootFile = projectPath + "/flake.nix";

  programs = {
    # nix
    alejandra.enable = true;
    deadnix.enable = true;
    statix.enable = true;
    prettier.enable = true;
    # python
    black.enable = true;
    # c
    clang-format.enable = true;
  };
}
