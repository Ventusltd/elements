# Elements

Built 2026-09-15T19:18:47Z from the block register generated 2026-09-15T18:28:26.149Z (sha256 `d356562b2e8f`) and the numbered database of 250,174 lines. Keys are the estate's permanent keys; none is invented. See catalogue/provenance.json.

| key | title | kind | category | state | functions | description |
|---|---|---|---|---|---|---|
| `block:At` | Allowed technologies | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 3 different values are in use; which is true is a decision. |
| `block:Ek` | Earth km | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Hr` | Hit radius edge px | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Hi` | Hit radius vertex px | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:L` | Limit | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Mr` | Max resources | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Mt` | Max tries | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Ri` | Repd ids | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Rp` | Repd page | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:Sm` | Solar min exclusive | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:S` | Statuses | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 2 different values are in use; which is true is a decision. |
| `block:T` | Technologies | constant | Constants and vocabularies | UNSETTLED | 0 | A value globalgrid2050 architecture development must agree on. 4 different values are in use; which is true is a decision. |
| `block:Gc` | Distance and bearing | engine | Geodesy and distance | SETTLED | 2 | The one haversine: distance and bearing between two points, with the three named earth radii (atlas, UK, mean). Every other copy of distanceKm should import from here. |
| `block:Ga` | Area and perimeter | engine | Geodesy and distance | SETTLED | 4 | Area of a polygon, perimeter of a line, area of a circle cap, in square kilometres. |
| `block:Gs` | Circles and shapes on the map | engine | Geodesy and distance | SETTLED | 2 | Points around a circle on the earth, for drawing search radii and zones. |
| `block:Gg` | GeoJSON helpers | engine | Geodesy and distance | SETTLED | 1 | Reading and writing GeoJSON features without losing coordinates. |
| `block:Vg` | Geodesy (v9 atlas copy) | engine | Geodesy and distance | SETTLED | 0 | The geodesy copy carried by the v9 atlas cartridges, byte-identical to the engine's. |
| `block:Vn` | Nearest substation search | engine | Geodesy and distance | SETTLED | 2 | Finds the nearest substations and lines to a point, the search the atlas runs on every click. |
| `block:Nt` | Grid network topology | engine | Grid network and electrical | SETTLED | 1 | Which substations connect to which lines, as a graph. |
| `block:Ed` | Electrical distance | engine | Grid network and electrical | SETTLED | 0 | Distance along the network rather than as the crow flies. |
| `block:Re` | Line and transformer ratings | engine | Grid network and electrical | SETTLED | 0 | How much a line or transformer can carry, by season. |
| `block:Ce` | Cable corridor estimate | engine | Connections and capacity | SETTLED | 0 | Length and cost of a cable corridor from a site to a connection point. |
| `block:Pf` | Published fault level | engine | Grid network and electrical | SETTLED | 4 | Fault level as each network operator publishes it; never calculated here. |
| `block:El` | Electrification demand | engine | Connections and capacity | SETTLED | 8 | Demand added when heat and transport go electric. |
| `block:Fc` | Firm capacity | engine | Connections and capacity | SETTLED | 7 | Capacity that can be relied on after the largest single loss. |
| `block:Dd` | Diversified demand | engine | Connections and capacity | SETTLED | 7 | Demand after allowing for loads that do not peak together. |
| `block:Cc` | Connection capacity | engine | Connections and capacity | SETTLED | 6 | Whether a site can connect and how much, from the ratings and the demand. |
| `block:Ro` | Route obstacles | engine | Connections and capacity | SETTLED | 3 | Roads, rails, rivers and buildings a route must cross. |
| `block:Ie` | Interconnector economics | engine | Connections and capacity | SETTLED | 8 | Value of moving power between markets. |
| `block:Po` | Power factor | engine | Grid network and electrical | SETTLED | 6 | Real, reactive and apparent power. |
| `block:Vd` | Voltage drop | engine | Grid network and electrical | SETTLED | 7 | Voltage lost along a cable for a given load. |
| `block:Sp` | streaming-parquet-bridge | cartridge | Map cartridges | SETTLED | 17 | A plug-in part of the GridAtlas map. |
| `block:Ug` | uk-gazetteer-flyto | cartridge | Map cartridges | SETTLED | 24 | A plug-in part of the GridAtlas map. |
| `block:Ss` | sld-sandbox | cartridge | Map cartridges | SETTLED | 24 | A plug-in part of the GridAtlas map. |
| `block:Si` | substation-intelligence | cartridge | Map cartridges | SETTLED | 24 | A plug-in part of the GridAtlas map. |
| `block:A` | Airports | layer | Map layers | SETTLED | 1 | A data layer drawn on the GridAtlas map. |
| `block:D` | Datacentres | layer | Map layers | SETTLED | 1 | A data layer drawn on the GridAtlas map. |
| `block:G1` | Grid 132 kV | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:G2` | Grid 220 kV | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:Gr` | Grid 275 kV | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:G4` | Grid 400 kV | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:G6` | Grid 66 kV | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:Gri` | Grid substations | layer | Map layers | SETTLED | 0 | A data layer drawn on the GridAtlas map. |
| `block:Io` | Industrial offtakers | layer | Map layers | SETTLED | 3 | A data layer drawn on the GridAtlas map. |
| `block:Pp` | Power plants | layer | Map layers | SETTLED | 1 | A data layer drawn on the GridAtlas map. |
| `block:R` | Railways | layer | Map layers | SETTLED | 2 | A data layer drawn on the GridAtlas map. |
| `block:Dt` | The MAP button (deep-link contract) | deeplink | Deep links and arrival | SETTLED | 24 | The contract every MAP link obeys, so a link always arrives on the right feature. |
| `block:Ps` | Place search and arrival | cartridge | Deep links and arrival |  | 21 | Search any UK place or project, fly the map there, and arrive on the exact feature a deep link names. |
| `block:Ra` | REPD Grid Atlas core engine (v3 to v8) | app | Map cartridges |  | 24 | The earlier all-in-one map engine that the cartridges replaced: layers, popups, radius tools and the substation curtain in one file. Kept as the ancestor of the current parts. |
| `block:Cg` | Cable trench geometry | app | Solar, BESS and cables |  | 24 | Lays cables out in a trench: spacing, burial depth, group geometry and the drawing of it. |
| `block:Sb` | Solar and BESS single-line sandbox | app | Solar, BESS and cables |  | 24 | Design a solar or battery site on the map with its single-line diagram, logistics presets and financial view. |
| `block:St` | Solar electrical topology (text engine) | app | Solar, BESS and cables |  | 24 | The text-based calculator for solar electrical topology: strings, inverters, transformers. |
| `block:Pn` | Pipeline News app | app | Pipeline News |  | 24 | The Pipeline News page itself: boot, engine genome panel, site links and rendering. |
| `block:Gp` | Grid proximity panel | app | Pipeline News |  | 24 | For each pipeline project, how far it is from the grid and from which substation. |
| `block:Wf` | Wider fleet panel | app | Pipeline News |  | 21 | The other projects of the same developer, with links into the atlas. |
| `block:Ln` | Live news discovery | tool | Pipeline News |  | 24 | Finds and checks new grid-connection news before it is published. |
| `block:Tp` | Teleprinter controls | cartridge | Pages and interface |  | 24 | The ticker-style controls that print the atlas's state as it changes. |
| `block:Em` | Site menu bar | tool | Pages and interface |  | 24 | The shared FILE / EDIT / VIEW / SCOPE / GRID / ABOUT bar on every page of globalgrid2050 architecture development. |
| `block:Mb` | Atlas menu bar | cartridge | Pages and interface |  | 0 | The atlas's own menu: layer names, groups and labels. |
| `block:Sa` | Satellite imagery | cartridge | Map layers |  | 24 | Ordering and checking satellite scenes over a site. |
| `block:Pr` | Proofs and checks | tool | Proofs and checks |  | 24 | Scripts that prove the other code: proofs, verifiers, mobile-UI checks, comparisons. |
| `block:Gn` | Genome and spiders | tool | Proofs and checks |  | 24 | The spiders that read globalgrid2050 architecture development and draw its graphs. |
| `block:Dc` | Data centres and offtakers data tools | tool | Map layers |  | 24 | Scripts that build the data centre, industrial offtaker and company datasets. |
| `block:x64` | Run study | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-five-hour-study/run_study.py. |
| `block:x66` | Watchdog | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-hourly-watchdog/watchdog.py. |
| `block:x68` | Watchdog | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-actions-watchdog/watchdog.py. |
| `block:x74` | Review | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-hourly-logic-review/review.py. |
| `block:x76` | Build prompt | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-gpt-reasoning-timer/build_prompt.py. |
| `block:x78` | Render response | auto | Other tools |  | 6 | Functions from chatgpt-audits automation/{stamp}-gpt-reasoning-timer/render_response.py. |
| `block:x80` | Clicker | auto | Other tools |  | 6 | Functions from claude familiars/clicker.py. |
| `block:x82` | Localai | auto | Other tools |  | 6 | Functions from claude familiars/localai.py. |
| `block:x84` | Runners | auto | Other tools |  | 6 | Functions from claude familiars/runners.py. |
| `block:x85` | Summon | auto | Other tools |  | 6 | Functions from claude familiars/summon.py. |
| `block:x86` | Triage | auto | Other tools |  | 6 | Functions from claude familiars/triage.py. |
| `block:x89` | Render session markdown | auto | Other tools |  | 6 | Functions from claude logs/tools/render_session_markdown.py. |
| `block:x91` | Ci history mine | auto | Other tools |  | 6 | Functions from claude scripts/ci_history_mine.py. |
| `block:x92` | Clean clone byte survey | auto | Other tools |  | 6 | Functions from claude scripts/clean_clone_byte_survey.py. |
| `block:x93` | Estate link crawl | auto | Other tools |  | 6 | Functions from claude scripts/estate_link_crawl.py. |
| `block:x101` | Deep | auto | Other tools |  | 6 | Functions from claude sessions/{stamp}-estate-and-corridor/scripts/deep.py. |
| `block:x109` | Router | auto | Other tools |  | 6 | Functions from claude sessions/{stamp}-estate-and-corridor/scripts/router.py. |
| `block:x116` | Engine | auto | Other tools |  | 6 | Functions from claude sessions/{stamp}-skin-architecture/prototype/engine.js. |
| `block:x117` | Index | auto | Other tools |  | 6 | Functions from claude sessions/{stamp}-skin-architecture/prototype/index.html. |
| `block:x126` | Selftest | auto | Other tools |  | 6 | Functions from cvaa tools/selftest.mjs. |
| `block:x128` | App | auto | Other tools |  | 6 | Functions from data-federation-map-for-globalgrid2050-all-repos live_sandbox/federation_control_ledger/app.js. |
| `block:x129` | Focus default | auto | Other tools |  | 3 | Functions from data-federation-map-for-globalgrid2050-all-repos live_sandbox/federation_control_ledger/focus-default.js. |
| `block:x130` | Build declared cartridges | auto | Other tools |  | 6 | Functions from data-federation-map-for-globalgrid2050-all-repos scripts/build_declared_cartridges.py. |
| `block:x131` | Build federation map | auto | Other tools |  | 6 | Functions from data-federation-map-for-globalgrid2050-all-repos scripts/build_federation_map.py. |
| `block:x132` | Publish federation json | auto | Other tools |  | 6 | Functions from data-federation-map-for-globalgrid2050-all-repos scripts/publish_federation_json.py. |
| `block:x148` | Backfill generation aggregates year v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/backfill_generation_aggregates_year_v6.py. |
| `block:x150` | Backfill generation fuelhh halfhourly all months v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/backfill_generation_fuelhh_halfhourly_all_months_v6.py. |
| `block:x151` | Backfill generation sources year v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/backfill_generation_sources_year_v6.py. |
| `block:x158` | Build generation heartbeat mvp | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/build_generation_heartbeat_mvp.py. |
| `block:x159` | Build homepage catalogue | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/build_homepage_catalogue.py. |
| `block:x160` | Build news feed v9 5 1 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/build_news_feed_v9_5_1.py. |
| `block:x162` | Build project identity v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/build_project_identity_v6.py. |
| `block:x167` | Catalogue gridatlas v9 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/catalogue_gridatlas_v9.py. |
| `block:x174` | Compare uk energy v5 v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/compare_uk_energy_v5_v6.py. |
| `block:x180` | Document uk energy trackers | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/document_uk_energy_trackers.py. |
| `block:x184` | Download ons mwh energy use v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/download_ons_mwh_energy_use_v6.py. |
| `block:x185` | Download pvlive solar history | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/download_pvlive_solar_history.py. |
| `block:x187` | Fetch generation mw year staged | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/fetch_generation_mw_year_staged.py. |
| `block:x188` | Fetch pvlive solar candidate v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/fetch_pvlive_solar_candidate_v6.py. |
| `block:x203` | Gridbot app repo bootstrap | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_app_repo_bootstrap.py. |
| `block:x208` | Gridbot deprecated tracker stale data audit | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_deprecated_tracker_stale_data_audit.py. |
| `block:x210` | Gridbot feature installer | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_feature_installer.py. |
| `block:x212` | Gridbot generation history solar | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_history_solar.py. |
| `block:x213` | Gridbot generation history solar recent | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_history_solar_recent.py. |
| `block:x215` | Gridbot generation history v6 2 backup mirror | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_history_v6_2_backup_mirror.py. |
| `block:x216` | Gridbot generation interconnector split | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_interconnector_split.py. |
| `block:x217` | Gridbot generation mwh active v6 source audit | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_mwh_active_v6_source_audit.py. |
| `block:x218` | Gridbot generation mwh interconnector split v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_mwh_interconnector_split_v6.py. |
| `block:x219` | Gridbot generation mwh interconnector ui guard | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_generation_mwh_interconnector_ui_guard.py. |
| `block:x225` | Gridbot london solar daylight geometry | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_london_solar_daylight_geometry.py. |
| `block:x226` | Gridbot mega upgrade | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_mega_upgrade.py. |
| `block:x227` | Gridbot modularise employers requirements | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_modularise_employers_requirements.py. |
| `block:x232` | Gridbot root homepage directory audit | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_root_homepage_directory_audit.py. |
| `block:x237` | Gridbot solar historic backfill | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_solar_historic_backfill.py. |
| `block:x239` | Gridbot solar monthly backfill | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_solar_monthly_backfill.py. |
| `block:x240` | Gridbot solar peak integrity audit | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_solar_peak_integrity_audit.py. |
| `block:x244` | Gridbot v6 same slot reconciliation audit | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/gridbot_v6_same_slot_reconciliation_audit.py. |
| `block:x245` | Inspect data science discipline | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/inspect_data_science_discipline.py. |
| `block:x247` | Major project news v5 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/major_project_news_v5.py. |
| `block:x248` | Major project news v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/major_project_news_v6.py. |
| `block:x249` | Major project news v6 hardened | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/major_project_news_v6_hardened.py. |
| `block:x254` | Modularize v3 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/modularize_v3.py. |
| `block:x258` | Patch v3 price history correctness | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/patch_v3_price_history_correctness.py. |
| `block:x278` | Repair public grid study period selector | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repair_public_grid_study_period_selector.py. |
| `block:x284` | Repair v6 electricity annual year selector | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repair_v6_electricity_annual_year_selector.py. |
| `block:x285` | Repair v6 half hourly short window modes | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repair_v6_half_hourly_short_window_modes.py. |
| `block:x290` | Repd sources v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repd_sources_v6.py. |
| `block:x291` | Repd updater | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repd_updater.py. |
| `block:x301` | Test v6 price history accuracy | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/test_v6_price_history_accuracy.py. |
| `block:x308` | Track repository size | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/track_repository_size.py. |
| `block:x309` | Update commodities v5 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_commodities_v5.py. |
| `block:x316` | Update uk frequency daily v5 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_uk_frequency_daily_v5.py. |
| `block:x317` | Update uk frequency v5 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_uk_frequency_v5.py. |
| `block:x320` | Update uk price | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_uk_price.py. |
| `block:x323` | Update uk price v6 | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_uk_price_v6.py. |
| `block:x325` | Update v6 transport energy sources | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/update_v6_transport_energy_sources.py. |
| `block:x329` | V6 complex upgrade installer | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/v6_complex_upgrade_installer.py. |
| `block:x340` | Atlas v9 | auto | Other tools |  | 6 | Functions from gridatlas atlas/releases/{stamp}-atlas-v9/assets/atlas-v9.mjs. |
| `block:x341` | Data gridatlas client | auto | Other tools |  | 6 | Functions from gridatlas atlas/releases/{stamp}-atlas-v9/assets/data-gridatlas-client.mjs. |
| `block:x342` | Repd address flyto | auto | Other tools |  | 6 | Functions from gridatlas atlas/releases/{stamp}-atlas-v9/cartridges/{stamp}-repd-address-flyto.mjs. |
| `block:x344` | V9 parquet fetch bridge | auto | Other tools |  | 6 | Functions from gridatlas atlas/releases/{stamp}-atlas-v9/v9-parquet-fetch-bridge.js. |
| `block:x349` | Browser proof | auto | Other tools |  | 6 | Functions from gridatlas atlas/testcode/{stamp}/browser-proof.py. |
| `block:x352` | Index | auto | Other tools |  | 6 | Functions from gridatlas atlas/world/index.html. |
| `block:x355` | Compile atlas v9 | auto | Other tools |  | 6 | Functions from gridatlas compiler/{stamp}-compile-atlas-v9.py. |
| `block:x356` | Compile atlas v9 live | auto | Other tools |  | 6 | Functions from gridatlas compiler/{stamp}-compile-atlas-v9-live.py. |
| `block:x357` | Build map ready v9 | auto | Other tools |  | 6 | Functions from gridatlas compiler/{stamp}-build-map-ready-v9.py. |
| `block:x359` | Local arrival grid | auto | Other tools |  | 4 | Functions from gridatlas local-arrival-grid.mjs. |
| `block:x370` | Reconcile offshore coordinates | auto | Other tools |  | 6 | Functions from gridatlas tools/offshore/reconcile_offshore_coordinates.py. |
| `block:x383` | Advance | auto | Other tools |  | 6 | Functions from gridatlas tools/scope/advance.mjs. |
| `block:x385` | Lib | auto | Other tools |  | 6 | Functions from gridatlas tools/scope/lib.mjs. |
| `block:x386` | Loop | auto | Other tools |  | 6 | Functions from gridatlas tools/scope/loop.mjs. |
| `block:x407` | Compile index | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-index.mjs. |
| `block:x408` | Compile v8 fast | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-fast.mjs. |
| `block:x409` | Compile v8 live news | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-live-news.mjs. |
| `block:x410` | Compile v8 news chronology | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-news-chronology.mjs. |
| `block:x411` | Compile v8 mobile orientation | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-mobile-orientation.mjs. |
| `block:x412` | Compile v8 sector intelligence | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-sector-intelligence.mjs. |
| `block:x413` | Compile v8 federated relationships | auto | Other tools |  | 6 | Functions from pipelinenews index/{stamp}-compile-v8-federated-relationships.mjs. |
| `block:x419` | V8 fast runtime | auto | Other tools |  | 6 | Functions from pipelinenews releases/javascript/{stamp}-v8-fast-runtime.js. |
| `block:x421` | Projects v9 5 1 | auto | Other tools |  | 6 | Functions from pipelinenews releases/javascript/{stamp}-projects-v9-5-1.js. |
| `block:x442` | Proof | auto | Other tools |  | 3 | Functions from pipelinenews tools/intelligence/cartridges/table-locality-sort/proof.mjs. |
| `block:x446` | Common | auto | Other tools |  | 6 | Functions from pipelinenews tools/intelligence/common.py. |
| `block:x448` | Release builder | auto | Other tools |  | 6 | Functions from pipelinenews tools/intelligence/release_builder.py. |
| `block:x460` | Build pages promotion wrapper | auto | Other tools |  | 6 | Functions from pipelinenews tools/publication/build_pages_promotion_wrapper.py. |
| `block:x461` | Pages release classifier | auto | Other tools |  | 6 | Functions from pipelinenews tools/publication/pages_release_classifier.py. |
| `block:x465` | Test pages promotion tooling | auto | Other tools |  | 6 | Functions from pipelinenews tools/publication/test_pages_promotion_tooling.py. |
| `block:x466` | Test pages release classifier | auto | Other tools |  | 6 | Functions from pipelinenews tools/publication/test_pages_release_classifier.py. |
| `block:x467` | Test release builder applicability | auto | Other tools |  | 6 | Functions from pipelinenews tools/publication/test_release_builder_applicability.py. |
| `block:x474` | Build registry | auto | Other tools |  | 6 | Functions from registry_of_all_content_in_repos_and_dependencies scripts/build_registry.py. |
| `block:x488` | Server | auto | Other tools |  | 6 | Functions from star-maker machinery/bench/server.mjs. |
| `block:x489` | Starmaker | auto | Other tools |  | 6 | Functions from star-maker machinery/bench/starmaker.mjs. |
| `block:x540` | Test control plane | auto | Other tools |  | 6 | Functions from v11 tests/test_control_plane.py. |
| `block:x542` | Index | auto | Other tools |  | 6 | Functions from ventus-grid-engine genome/index.html. |
| `block:x545` | Atlas v8 polish | auto | Other tools |  | 6 | Functions from youengineer-code-review civilisation-atlas-v8/atlas-v8-polish.js. |
| `block:x547` | Atlas map | auto | Other tools |  | 6 | Functions from youengineer-code-review civilisation-atlas/atlas-map.js. |
| `block:x548` | Atlas ui | auto | Other tools |  | 6 | Functions from youengineer-code-review civilisation-atlas/atlas-ui.js. |
| `block:x550` | Civilisation map | auto | Other tools |  | 6 | Functions from youengineer-code-review civilisation-map.js. |
| `block:x551` | Myth reader | auto | Other tools |  | 6 | Functions from youengineer-code-review myth-reader.js. |
| `block:x554` | Script | auto | Other tools |  | 6 | Functions from youengineer-code-review world-cup-knockout/script.js. |
| `block:x563` | Atlas receiver v9 7 | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/pipeline/scripts/core/atlas-receiver-v9-7.js. |
| `block:x592` | Newspaper v9 5 | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/pipeline/scripts/plugins/newspaper-v9-5.js. |
| `block:x602` | Projects v9 4 | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/pipeline/scripts/plugins/projects-v9-4.js. |
| `block:x603` | Projects v9 5 1 | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/pipeline/scripts/plugins/projects-v9-5-1.js. |
| `block:x604` | Projects v9 5 | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/pipeline/scripts/plugins/projects-v9-5.js. |
| `block:x618` | Index | auto | Other tools |  | 6 | Functions from globalgrid2050 cable_selection/index.html. |
| `block:x654` | Homepage v095 | auto | Other tools |  | 4 | Functions from globalgrid2050 homepage_versions/homepage_v095.html. |
| `block:x655` | Homepage v098 | auto | Other tools |  | 6 | Functions from globalgrid2050 homepage_versions/homepage_v098.html. |
| `block:x658` | Controls | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/teleprinter/controls.js. |
| `block:x659` | Print screen | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/teleprinter/print-screen.js. |
| `block:x672` | Earth | auto | Other tools |  | 6 | Functions from globalgrid2050 marketing/earth.html. |
| `block:x678` | Host | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/tool-layers/host.js. |
| `block:x681` | Readiness | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/tool-layers/readiness.js. |
| `block:x709` | Frequency history ui | auto | Other tools |  | 6 | Functions from globalgrid2050 uk_energy_tracking_v5/frequency-history-ui.js. |
| `block:x744` | Projects v9 5 1 | auto | Other tools |  | 6 | Functions from globalgrid2050 uk_renewables_pipeline/{stamp}/scripts/plugins/projects-v9-5-1.js. |
| `block:x749` | Projects v9 8 | auto | Other tools |  | 6 | Functions from globalgrid2050 uk_renewables_pipeline/{stamp}/scripts/plugins/projects-v9-8.js. |
| `block:x756` | Projects v9 6 | auto | Other tools |  | 6 | Functions from globalgrid2050 uk_renewables_pipeline/v9.6/scripts/plugins/projects-v9-6.js. |
| `block:x760` | Dashboard | auto | Other tools |  | 6 | Functions from globalgrid2050-homepage assets/dashboard.js. |
| `block:x764` | Bench gpu | auto | Other tools |  | 6 | Functions from gpu-drivers-for-global-grid claude/bench-gpu.mjs. |
| `block:x776` | Geodesy | auto | Other tools |  | 6 | Functions from grid-distance-maths src/geodesy.mjs. |
| `block:x777` | Geodesy | auto | Other tools |  | 6 | Functions from grid-distance-maths src/geodesy.py. |
| `block:x783` | Select build plan | auto | Other tools |  | 6 | Functions from gridatlas {stamp}-gridatlas-next-version-builders/tools/{stamp}-select-build-plan.mjs. |
| `block:x784` | Place postcode search | auto | Other tools |  | 6 | Functions from gridatlas atlas/cartridges/{stamp}-place-postcode-search.js. |
| `block:x785` | Neon substation links v9 6 | auto | Other tools |  | 6 | Functions from gridatlas atlas/cartridges/{stamp}-neon-substation-links-v9-6.js. |
| `block:x837` | Core | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/core.js. |
| `block:x839` | Index | auto | Other tools |  | 5 | Functions from globalgrid2050 testcode/{stamp}/v03-particle-universe/index.html. |
| `block:x847` | Journey | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/journey.js. |
| `block:x849` | Index | auto | Other tools |  | 6 | Functions from testcode table/{stamp}T144622Z-block-page-rnd/index.html. |
| `block:x881` | Concept compute | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/concept_compute.py. |
| `block:x897` | Bench | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/proof/bench.mjs. |
| `block:x907` | Ui | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/ui.js. |
| `block:x912` | Night tests | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/ci/night-tests.mjs. |
| `block:x913` | Build sun | auto | Other tools |  | 6 | Functions from star-solar-star scripts/build_sun.py. |
| `block:x918` | Test build sun | auto | Other tools |  | 6 | Functions from star-solar-star testcode/{stamp}/test_build_sun.py. |
| `block:x920` | Test country star | auto | Other tools |  | 6 | Functions from star-solar-star testcode/{stamp}/test_country_star.py. |
| `block:x923` | Build state | auto | Other tools |  | 6 | Functions from star-quantum-twin build_state.mjs. |
| `block:x927` | Quantum | auto | Other tools |  | 6 | Functions from star-quantum-twin quantum.js. |
| `block:x933` | Build | auto | Other tools |  | 6 | Functions from star-sector-star proof/build.py. |
| `block:x936` | Star | auto | Other tools |  | 6 | Functions from star-sector-star star.js. |
| `block:x939` | App | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/app.mjs. |
| `block:x940` | Model | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/model.mjs. |
| `block:x946` | Star checks | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/ci/star_checks.py. |
| `block:x947` | Test star checks | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/ci/test_star_checks.py. |
| `block:x951` | Test integrity | auto | Other tools |  | 6 | Functions from star-solar-star testcode/{stamp}/test_integrity.py. |
| `block:x953` | Test publication | auto | Other tools |  | 6 | Functions from star-solar-star tests/test_publication.py. |
| `block:x957` | Lib | auto | Other tools |  | 6 | Functions from galaxies-wafers lib.mjs. |
| `block:x958` | Checks | auto | Other tools |  | 1 | Functions from galaxies-wafers proof/checks.mjs. |
| `block:x961` | Layers panel | auto | Other tools |  | 6 | Functions from galaxies-wafers layers-panel.mjs. |
| `block:x968` | Layers panel | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/04-400kv-engine/layers-panel.mjs. |
| `block:x970` | Engines | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/06-stars-as-engines/engines.mjs. |
| `block:x973` | Table | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/05-periodic-table/table.mjs. |
| `block:x975` | Code particle | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/03-code-particle/code-particle.mjs. |
| `block:x976` | Index | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/10-ground-bridge/index.html. |
| `block:x978` | App | auto | Other tools |  | 6 | Functions from galaxies-wafers iterations/08-space-and-time/app.mjs. |
| `block:x981` | Code card | auto | Other tools |  | 5 | Functions from galaxies-wafers iterations/07-code-card/code-card.mjs. |
| `block:x986` | Make publication | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/make_publication.py. |
| `block:x987` | Repin v9 gates | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/repin_v9_gates.py. |
| `block:x988` | Test make publication | auto | Other tools |  | 6 | Functions from globalgrid2050 scripts/test_make_publication.py. |
| `block:x990` | Physics | auto | Other tools |  | 6 | Functions from globalgrid2050 testcode/{stamp}/physics.mjs. |
| `block:x992` | Bond validator | auto | Other tools |  | 6 | Functions from testcode sandbox/{stamp}-galaxy-bond/bond_validator.py. |
| `block:x994` | Test bond validator | auto | Other tools |  | 6 | Functions from testcode sandbox/{stamp}-galaxy-bond/test_bond_validator.py. |
| `block:x996` | Electrification model | auto | Other tools |  | 6 | Functions from ventus-grid-engine engine/electrification-model.js. |
