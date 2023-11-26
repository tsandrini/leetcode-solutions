# --- nix/lib/default.nix
{
  pkgs,
  lib,
  inputs,
  projectPath ? ./..,
  ...
}: let
  inherit (bootstrap) mapModules';

  bootstrap = import ./_bootstrap-lib.nix {inherit lib;};

  leetcode-solutions = lib.makeExtensible (self:
    with self;
      mapModules' ./. (file:
        import file {
          inherit pkgs lib self inputs projectPath;
        }));
in
  leetcode-solutions.extend
  (_self: super: lib.foldr (a: b: a // b) {} (lib.attrValues super))
